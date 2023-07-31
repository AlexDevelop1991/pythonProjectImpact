import telebot
from telebot import types
import random

TOKEN = '5616580938:AAFUHuYdqqbV2CmKXMoSQjYMzeJuLKSU81E'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Man♂')
    item2 = types.KeyboardButton('Woman♀')
    item3 = types.KeyboardButton('Child/Boy👦')
    item4 = types.KeyboardButton('Child/Girl👧')
    item5 = types.KeyboardButton('Byu')
    markup.add(item1, item2, item3, item4, item5)
    bot.send_message(message.chat.id, 'Hello I am Chat_Bot🤖 can help you choose sneakers👟\n Choose your Gender: ',
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def dialog(message):
    import request_and_soup
    if message.text == 'Man♂':
        bot.send_message(message.chat.id, 'Thank you for using my services🤖', parse_mode='html')
        bot.send_message(message.chat.id, random.choice(request_and_soup.request_sneakers_man()))

    elif message.text == 'Woman♀':
        bot.send_message(message.chat.id, 'Thank you for using my services🤖', parse_mode='html')
        bot.send_message(message.chat.id, random.choice(request_and_soup.request_sneakers_woman()))

    elif message.text == 'Child/Boy👦':
        bot.send_message(message.chat.id, 'Thank you for using my services🤖', parse_mode='html')
        bot.send_message(message.chat.id, random.choice(request_and_soup.request_sneakers_boy()))

    elif message.text == 'Child/Girl👧':
        bot.send_message(message.chat.id, 'Thank you for using my services🤖', parse_mode='html')
        bot.send_message(message.chat.id, random.choice(request_and_soup.request_sneakers_girl()))

    elif message.text == 'Byu':
        bot.send_message(message.chat.id, 'Bye have a nice day')

    else:
        bot.send_message(message.chat.id, "Sorry service not available")


run_bot = bot.polling(non_stop=True)