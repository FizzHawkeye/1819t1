"""
This is the script that receives messages from Telegram,
and sends requests to the server.

Usage:
$ python3 bot.py 50000

(The argument specifies the port on which the server is listening)
"""
import sys
import socket
import threading
import json
import base64
from io import BytesIO
from PIL import Image
from queue import Queue
import requests
import time
import telepot
from telepot.loop import MessageLoop

# First queue for transferring image from bot thread to client thread
queue1 = Queue()

# Second queue for transferring results from server to the response thread
queue2 = Queue()


def handle(msg):
    """
    A function that will be invoked when a message is
    recevied by the bot
    """
    content_type, chat_type, chat_id = telepot.glance(msg)
    print("Message received")

    # Use the chat_id to name the image
    image_file = "{}.png".format(chat_id)

    if content_type == "text":
        # If content type is text, it should contain a URL to an image
        content = msg["text"]
        if not content.startswith("http"):
            return

        # Download the image and save to a local file
        image_data = requests.get(content).content
        with open(image_file, 'wb') as outfile:
            outfile.write(image_data)

    elif content_type == "photo":
        # If content type is photo, download photo from Telegram
        bot.download_file(msg['photo'][-1]['file_id'], image_file)

    else:
        return

    # Submit the image and the chat_id to queue1
    queue1.put((Image.open(image_file), chat_id))


def client_thread():
    """
    A thread that receives images from queue1, and communicate
    with the server to get predictions on the image.
    """
    print("Client thread started")
    while True:
        # Get data from queue1 continuously
        image, chat_id = queue1.get()
        print("Got an image from queue1")

        # Encode the received image into base64 string
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        encoded_image = base64.b64encode(buffered.getvalue())

        # Connect to the server
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.settimeout(5)
        soc.connect(("localhost", int(sys.argv[1])))

        # Prepare the data to be sent
        # JSON encode the data, and then add the delimiter
        # (##END##) to the end of the string
        # and then send it to the server
        data = {
            'image': encoded_image.decode("utf-8"),
            'chat_id': chat_id
        }
        data = json.dumps(data) + "##END##"
        soc.sendall(data.encode("utf-8"))

        # Receive result from the server
        data = ""
        while True:
            part = soc.recv(1024)
            data = data + part.decode("utf-8")
            if "##END##" in data:
                break

        # Submit the result to queue2, for returning
        # the answer to the user in Telegram
        data = data.replace("##END##", "")
        queue2.put(json.loads(data))
        soc.close()


def response_thread():
    """
    A thread that takes results from the client thread,
    then format a message and send it back to the user.
    """
    print("Response thread started")

    while True:
        # Keep getting data from queue2
        data = queue2.get()
        print(data)
        chat_id = data['chat_id']
        predictions = data['predictions']

        # Prepare the response message to the user
        reply = ""
        for i, pred in enumerate(predictions):
            reply += "{}. {} ({:.4f})\n".format(
                i+1, pred['label'], pred['proba'])

        # Send the message back to the user
        bot.sendMessage(chat_id, reply)
        print("Message sent to user")


if __name__ == "__main__":
    
    # Start the threads
    threading.Thread(target=client_thread).start()
    threading.Thread(target=response_thread).start()

    # Povide your bot's token
    bot = telepot.Bot("__BOT_TOKEN__")
    MessageLoop(bot, handle).run_as_thread()
    print("Start handling messages from Telegram...")

    while True:
        time.sleep(10)
