from re import T
from telebot import types;

zero = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
zero_buttons = ['Lifecell', 'Vodafone', 'Kyivstar']
zero.add(*zero_buttons)


operator = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
operator_buttons = ['Так', 'Ні']
operator.add(*operator_buttons)


rings = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
rings_buttons = ['1', '2', '3', '4']
rings.add(*rings_buttons)


price = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
price_buttons = ['1', '2', '3']
price.add(*price_buttons)