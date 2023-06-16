import telebot;
import time;
from dotenv import load_dotenv;
from telebot import types;
import os;

# python-dotenv library is used for saving telegram token so it will not leak to network
load_dotenv()
bot = telebot.TeleBot(os.getenv("TOKEN"))


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text="Вітаємо в телеграм боті.")


def Work():
   '''This method is used for restarting bot if it crashed during work'''
   try:
     y = bot.polling(none_stop=True, interval=0.5)
     bot.polling(none_stop=True, interval=0.5)
     return y
   except:
      time.sleep(60)
      Work()

Work()