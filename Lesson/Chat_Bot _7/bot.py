import telebot
from telebot import types
import random

TOKEN = '5616580938:AAFUHuYdqqbV2CmKXMoSQjYMzeJuLKSU81E'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Man♂️')
    item2 = types.KeyboardButton('Woman♀️')
    item3 = types.KeyboardButton('Child/Boy👦')
    item4 = types.KeyboardButton('Child/Girl👧')
    item5 = types.KeyboardButton('Byu')
    markup.add(item1, item2, item3, item4, item5)
    bot.send_message(message.chat.id, 'Hello I am Chat_Bot🤖 can help you choose sneakers👟\n Choose your Gender: ',
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def dialog(message):
    if message.text == 'Man♂️':
        from request_and_soup import request_sneakers_man
        sneakers = request_sneakers_man()
        bot.send_message(message.chat.id, random.choice(sneakers))

    elif message.text == 'Woman♀️':
        from request_and_soup import request_sneakers_woman
        sneakers = request_sneakers_woman()
        bot.send_message(message.chat.id, random.choice(sneakers))

    elif message.text == 'Child/Boy👦':
        from request_and_soup import request_sneakers_boy
        sneakers = request_sneakers_boy()
        bot.send_message(message.chat.id, random.choice(sneakers))

    elif message.text == 'Child/Girl👧':
        from request_and_soup import request_sneakers_girl
        sneakers = request_sneakers_girl()
        bot.send_message(message.chat.id, random.choice(sneakers))

    elif message.text == 'Byu':
        bot.send_message(message.chat.id, 'Bye have a nice day')

    else:
        bot.send_message(message.chat.id, "I don't have an answer for that")


run_bot = bot.polling()