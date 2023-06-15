import telebot

import random

from telebot import types

bot = telebot.TeleBot('5616580938:AAFUHuYdqqbV2CmKXMoSQjYMzeJuLKSU81E')


@bot.message_handlers(commands=['start'])
def welcome(message):
    # Keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Random Number')
    item2 = types.KeyboardButton('How are you?')

    markup.add(item1, item2)

    bot.send_message(message.chat.id,
                     'Welcome, {0.first_name}!\nI am - <b>{1.first_name}</b>,'
                     'bot created for test. '.format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)
