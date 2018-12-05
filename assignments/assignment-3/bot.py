import time
import requests
import telepot
import logging
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardButton, InlineKeyboardMarkup

# Set up logging 
logging.basicConfig(level=logging.INFO)

# Server APIs
server = "http://localhost:8080"
api_register = server + "/register"
api_get_unrated_movie = server + "/get_unrated_movie"
api_rate_movie = server + "/rate_movie"
api_recommend = server + "/recommend"


def handle(msg):
    """
    A function that will be invoked when a message is
    recevied by the bot
    """
    text = msg.get("text", None)
    data = msg.get("data", None)

    if data is not None:
        # This is a message from a custom keyboard
        chat_id = msg["message"]["chat"]["id"]
        content_type = "data"
    elif text is not None:
        # This is a command sent from the user
        chat_id = msg["chat"]["id"]
        content_type = "text"
    else:
        content_type = "unknown"
    
    if content_type == "text":
        message = msg["text"]
        logging.info("Received from chat_id={}: {}".format(chat_id, message))

        if message == "/start":
            # Check against the server to see
            # if the user is new or not
            data = requests.post(api_register, json={"chat_id": chat_id}).json()
            if data["exists"] == 0:
                bot.sendMessage(chat_id, "Welcome!")
            else:
                bot.sendMessage(chat_id, "Welcome back!")

        elif message == "/rate":
            # Ask the server to return a random
            # movie, and ask the user to rate the movie
            data = requests.post(api_get_unrated_movie, json={"chat_id": chat_id}).json()
            msg = "{}: {}".format(data["title"], data["url"])
            bot.sendMessage(chat_id, msg)

            # Create custom keyboard for rating
            # Callback data contains the movie ID
            my_inline_keyboard = [[
                InlineKeyboardButton(text='1', callback_data='rate_movie_{}_1'.format(data["id"])),
                InlineKeyboardButton(text='2', callback_data='rate_movie_{}_2'.format(data["id"])),
                InlineKeyboardButton(text='3', callback_data='rate_movie_{}_3'.format(data["id"])),
                InlineKeyboardButton(text='4', callback_data='rate_movie_{}_4'.format(data["id"])),
                InlineKeyboardButton(text='5', callback_data='rate_movie_{}_5'.format(data["id"])),
            ]]
            keyboard = InlineKeyboardMarkup(inline_keyboard=my_inline_keyboard )
            bot.sendMessage(chat_id, "How do you rate this movie?", reply_markup=keyboard)

        elif message == "/recommend":
            # Ask the server to generate a list of
            # recommended movies to the user
            data = requests.post(api_recommend, json={"chat_id": chat_id, "top_n": 3}).json()
            if len(data["movies"]) == 0:
                bot.sendMessage(chat_id, "You have not rated enough movies, we cannot generate recommendation for you")
            else:
                # Send each recommended movie in a separate message
                for mov in data["movies"]:
                    msg = "{}: {}".format(mov["title"], mov["url"])
                    bot.sendMessage(chat_id, msg)

        else:
            # The input matches nothing
            bot.sendMessage(chat_id, "I don't understand your command.")

    elif content_type == "data":
        # Received rating from the user
        logging.info("Received rating: {}".format(data))
        parts = data.split("_")
        movie_id = int(parts[2])
        rating = int(parts[3])

        # Submit data to server
        data = {
            "chat_id": chat_id,
            "movie_id": movie_id,
            "rating": rating
        }
        requests.post(api_rate_movie, json=data)
        bot.sendMessage(chat_id, "Your rating is received!")


if __name__ == "__main__":
    
    # Povide your bot's token 
    bot = telepot.Bot("__BOT_TOKEN__")
    MessageLoop(bot, handle).run_as_thread()

    while True:
        time.sleep(10)
