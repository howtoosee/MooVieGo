import telebot
from telebot.types import ReplyKeyboardRemove, ReplyKeyboardMarkup

from load_env import load_env
from search import custom_search

# Bot Settings
env = load_env()
TOKEN = env['TELE_TOKEN']
bot = telebot.TeleBot(TOKEN)

# UI inputs
hideBoard = ReplyKeyboardRemove()  # function to hide inline keyboard
list_of_commands = []


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id,
        "Wanna watch movie? /movie \n" +
        "Know more about us? /about"
    )


@bot.message_handler(commands=['about'])
def about_us(message):
    bot.send_chat_action(message.chat.id, 'typing')  # Bot typing action
    bot.send_message(message.chat.id, "This is Us")


@bot.message_handler(commands=['movie'])
def movie(message):
    choice = ["yeh", "meh"]
    choice_select = ReplyKeyboardMarkup(one_time_keyboard=True)  # Converts list of stores to keyboard
    for i in choice:
        choice_select.add(i)

    bot.send_chat_action(message.chat.id, 'typing')  # Bot typing action
    final_choice = bot.send_message(message.chat.id, "legit wanna watch a movie???",
                                    reply_markup=choice_select)  # Send catch response

    bot.register_next_step_handler(final_choice, what_movie)


@bot.message_handler(func=lambda message: True)
def what_movie(message):
    choice = ["yeh", "meh"]
    if message.text in list_of_commands:  # Checks whether user selects another function
        check_reply(message)  # Starts new function if user selects another function midway
    else:
        cid = message.chat.id
        bot.send_chat_action(cid, 'typing')  # Bot typing action
        if message.text in choice:
            bot_response = "Ok what you wanna watch?"
            movie_name = bot.send_message(message.chat.id, bot_response,
                                          reply_markup=hideBoard)  # Removes inline keyboard
            bot.register_next_step_handler(movie_name, search_movie)
        else:
            bot.send_message(cid, "Invalid Input, Try Again")


def search_movie(message):
    term = message.text
    cid = message.chat.id
    res = custom_search(term.replace(" ", "+"))
    bot.send_message(cid, "Ok nah here are ur links:")
    ret_str = ""
    for item in res['items']:
        ret_str += "{}:\n{}\n\n".format(item['title'], item['link'])
    bot.send_message(cid, ret_str)
    bot.send_message(cid, "eNjOy!")


def check_reply(message):
    message_input = message.text
    if message_input == "/start":
        start_command(message)
    elif message_input == "/about":
        about_us(message)
    elif message_input == "/movie":
        movie(message)


bot.polling()
