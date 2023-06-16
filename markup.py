from telebot import types;

zero = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
var = ['Lifecell', 'Vodafone', 'Kyivstar']
zero.add(*var)


operator = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
var = ['Так', 'Ні']
operator.add(*var)


rings = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
var = ['1', '2', '3', '4']
rings.add(*var)


price = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
var = ['1', '2', '3']
price.add(*var)