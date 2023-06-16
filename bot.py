import os;
import time;
import telebot;
from dotenv import load_dotenv;
from telebot import types, custom_filters;
import markup as nav
from telebot.handler_backends import State, StatesGroup #States

# States storage
from telebot.storage import StateMemoryStorage

# python-dotenv library is used for saving telegram token so it will not leak to network
load_dotenv()

state_storage=StateMemoryStorage()
bot = telebot.TeleBot(os.getenv("TOKEN"))


user_dict = {}

# States group.
class OperatorPoll:
    def __init__(self, zero): 
        self.zero = zero
        self.operator = None
        self.rings = None
        self.rings_time = None
        self.network = None
        self.price = None


@bot.message_handler(commands=['life'])
def life(message):
    bot.register_next_step_handler(message, zero_q)
    bot.send_message(message.chat.id, text="Розпочнімо опитування. Питання №0: Яким оператором ви користуєтесь?", reply_markup=nav.zero)


def zero_q(message):
    zero = message.text
    user = OperatorPoll(zero)
    chat_id = message.chat.id
    user_dict[chat_id] = user
    if message.text not in ["Lifecell"]:
        bot.send_message(message.chat.id, text="Ми радимо вам перейти на тарифів Lifecell")
    else:
        bot.send_message(message.chat.id, text="Ми раді, що ви довіряєте нам. Продовжимо опитування, щоб підібрати для вас найкращий тариф")
    bot.send_message(message.chat.id, text="Питання №1.  Чи часто вам потрібно дзвонити на номери інших операторів?", reply_markup=nav.operator)
    bot.register_next_step_handler(message, operator_q)


def operator_q(message):
    chat_id = message.chat.id
    user_dict[chat_id].operator = message.text
    bot.send_message(message.chat.id, text="Питання №2. Як часто ви дзвоните? \n1. Кілька разів на місяць. \n2. Раз в тиждень. \n3. Кілька разів на тиждень. \n4. Кілька разів на день)", reply_markup=nav.rings)
    bot.register_next_step_handler(message, ring_q)


def ring_q(message):
    chat_id = message.chat.id
    user_dict[chat_id].rings = message.text
    bot.send_message(message.chat.id, text="Питання №3. Скільки часу тривають дзвінки? \n1.До трьох хвилин \n2. Десять хвилин \n3. Півгодини. \n4. Не кладу слухавку)", reply_markup=nav.rings)
    bot.register_next_step_handler(message, ring_time)


def ring_time(message):
    chat_id = message.chat.id
    user_dict[chat_id].rings_time = message.text
    bot.send_message(message.chat.id, text="Питання №4. Як ви використовуєте мобільні дані? \n1. Месенджері \n2. Дивлюсь відео, фільми. \n3. Роздаю на комп'ютер \n4.Тримаю ботоферму)", reply_markup=nav.rings)
    bot.register_next_step_handler(message, network)


def network(message):
    chat_id = message.chat.id
    user_dict[chat_id].network = message.text
    bot.send_message(message.chat.id, text="Питання №5. Скільки ви готові витратити на послуги мобільного зв'язку? \n1. До 200 грн \n2. 200-400 грн \n3. Стільки, скільки потрібно буде для моїх потреб", reply_markup=nav.price)
    bot.register_next_step_handler(message, price)


def price(message):
    chat_id = message.chat.id
    user_dict[chat_id].price = message.text
    bot.send_message(message.chat.id, text="Секундочку. Підбираємо тариф, який вам ідеально пасуватиме")
    text = calculation
    bot.send_message(chat_id, text=text)


def calculation(chat_id):
    userpoll = user_dict[chat_id]


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text="Вітаємо в телеграм боті.")


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, text="""Отже, ось що я вмію:
    /help -- ця команда перекине вас сюди. Тут ви можете дізнатись про мої функції;
    /life -- ця команда розпочне опитування, яке допоможе визначити, який тариф вам підійде
    /support -- """)


bot.polling(none_stop=True, interval=0.5)