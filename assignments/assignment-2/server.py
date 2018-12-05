"""
This is the server script. It accepts connections from clients,
receives data, generates predictions and sends respond to the client.

This script has two threads:
1) main thread: for accepting conenctions from clients
2) model thread: for communicating with the client and generating predictions

Usage:
$ python3 server.py 50000

(The argument specifies the port on which the server is listening)
"""
import sys
import threading
import socket
import time
import base64
import json
import tensorflow as tf
from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
from queue import Queue

# A queue for transferring client socket/address from
# main thread to the handler thread
queue = Queue()


class ModelThread(threading.Thread):
    """
    A class subclassing Thread for wrapping the
    data communication between the server and the client.

    The Keras model is pre-loaded in the constructor so that
    it can be used readily when a request is received from the client
    """

    def __init__(self, queue):
        # Must call the parent's constructor
        super(ModelThread, self).__init__()

        # Pre-load the Keras model
        self.model = ResNet50(weights='imagenet')
        
        # Get a reference of the tensorflow graph
        # This is necessary when using the model to do inference later
        self.graph = tf.get_default_graph()

        # A reference to the queue for getting client socket
        # from the main thread
        self.queue = queue
        print("Model thread has started.")
    
    def run(self):
        """
        Implement the run function, which will be executed when
        this thread is started

        Logic:
            1. Get a client socket/address pair from the queue
            2. Receive data from client until the delimiter is received
                (in our case we use ##END##)
            3. Decode the data and save the image to a local file
            4. Load the image, preprocess it, and feed it into the model
            5. Encode the predictions
            6. Send the result back to the client
            7. Close the client socket
            8. Go back to Step 1
        """
        while True:
            # Get client socket and client address from the queue
            client_socket, client_address = queue.get()
            print("Got {} from queue.".format(client_address))

            # Receive data from the client
            data = ""
            while True:
                part = client_socket.recv(1024)
                data = data + part.decode("utf-8")
                if "##END##" in data:
                    # Delimiter is received, we can stop receiving
                    break

            # Remove the delimiter from the data received,
            # and then decode the data and save the image
            data = data.replace("##END##", "")
            data = json.loads(data)
            image_data = base64.b64decode(data['image'])
            with open('image.png', 'wb') as outfile:
                outfile.write(image_data)

            # Load the image, preprocess it
            img = image.load_img('image.png', target_size=(224, 224))
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = preprocess_input(x)

            # Get predictions from the model
            with self.graph.as_default():
                preds = self.model.predict(x)
            decoded = decode_predictions(preds, top=5)[0]

            # Prepare the output to be sent to client
            output = {
                "predictions": [],
                "chat_id": data["chat_id"]
            }
            output["predictions"] = [
                {"label": label, "proba": float(proba)}
                for label_id, label, proba in decoded
            ]
            
            # Add the delimiter to the output data
            # and send the data back to the client
            out_data = json.dumps(output) + "##END##"
            client_socket.sendall(out_data.encode("utf-8"))
            print("Data sent to {}".format(client_address))

            # Close the client socket
            client_socket.close()

# Start the model thread
thread = ModelThread(queue)
thread.start()

# Create an INET socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to the host and a port
server_socket.bind(("localhost", int(sys.argv[1])))

# Listen for incoming connections from clients
server_socket.listen(10)

# An indefinite loop
while True:
    # accept connections from outside
    (client_socket, address) = server_socket.accept()
    print("Accepted connection from {}".format(address))

    # put the client socket and address into the queue
    # so that the model thread will receive them
    queue.put((client_socket, address))
