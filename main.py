from config import token
import telebot
from telebot import types

from pars import Parser

bot = telebot.TeleBot(token, skip_pending=True)

@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn1 = types.KeyboardButton("Bitcoin BTC")
	btn2 = types.KeyboardButton("Ethereum ETH")
	btn3 = types.KeyboardButton("BNB BNB")
	btn4 = types.KeyboardButton("Dogecoin DOGE")
	markup.add(btn1, btn2, btn3, btn4)
	bot.send_message(message.chat.id, text="Hello, {0.first_name}! This bot shows prices of cryptocurrencies".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):

	info = Parser.getAllInfo(message.text.replace(" ", ""))

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn1 = types.KeyboardButton("Bitcoin BTC")
	btn2 = types.KeyboardButton("Ethereum ETH")
	btn3 = types.KeyboardButton("BNB BNB")
	btn4 = types.KeyboardButton("Dogecoin DOGE")
	markup.add(btn1, btn2, btn3, btn4)
	bot.send_message(
		message.chat.id,
		text=f"{message.text}\n\
			Price: {info['price']}\n\
			Market Cup: {info['marketCup']}\n\
			Volume: {info['volume']}",
		reply_markup=markup
	)

bot.polling(none_stop=True)
