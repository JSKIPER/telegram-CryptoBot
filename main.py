import pars
import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token, skip_pending=True)

@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn1 = types.KeyboardButton("Bitcoin")
	btn2 = types.KeyboardButton("Ethereum")
	btn3 = types.KeyboardButton("BNB")
	btn4 = types.KeyboardButton("Dogecoin")
	markup.add(btn1, btn2, btn3, btn4)
	bot.send_message(message.chat.id, text="Hello, {0.first_name}! This bot shows prices of cryptocurrencies".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
	global price
	global value
	global market_cup
	if(message.text == "Bitcoin"):
		bitcoin = pars.parser(index= 1)
		price = bitcoin[0]
		market_cup = bitcoin[1]
		value = bitcoin[2]
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn1 = types.KeyboardButton("Price")
		btn2 = types.KeyboardButton("Market Cup")
		btn3 = types.KeyboardButton("Value")
		btn4 = types.KeyboardButton("Back")
		markup.add(btn1, btn2, btn3, btn4)
		bot.send_message(message.chat.id, text="Choose option", reply_markup=markup)


	elif(message.text == "Ethereum"):
		bitcoin = pars.parser(index= 2)
		price = bitcoin[0]
		market_cup = bitcoin[1]
		value = bitcoin[2]
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn1 = types.KeyboardButton("Price")
		btn2 = types.KeyboardButton("Market Cup")
		btn3 = types.KeyboardButton("Value")
		btn4 = types.KeyboardButton("Back")
		markup.add(btn1, btn2, btn3, btn4)
		bot.send_message(message.chat.id, text="Choose option", reply_markup=markup)



	elif(message.text == "BNB"):
		bitcoin = pars.parser(index= 4)
		price = bitcoin[0]
		market_cup = bitcoin[1]
		value = bitcoin[2]
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn1 = types.KeyboardButton("Price")
		btn2 = types.KeyboardButton("Market Cup")
		btn3 = types.KeyboardButton("Value")
		btn4 = types.KeyboardButton("Back")
		markup.add(btn1, btn2, btn3, btn4)
		bot.send_message(message.chat.id, text="Choose option", reply_markup=markup)



	elif(message.text == "Dogecoin"):
		bitcoin = pars.parser(index= 9)
		price = bitcoin[0]
		market_cup = bitcoin[1]
		value = bitcoin[2]
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn1 = types.KeyboardButton("Price")
		btn2 = types.KeyboardButton("Market Cup")
		btn3 = types.KeyboardButton("Value")
		btn4 = types.KeyboardButton("Back")
		markup.add(btn1, btn2, btn3, btn4)
		bot.send_message(message.chat.id, text="Choose option", reply_markup=markup)



	if(message.text == "Price"):
		bot.send_message(message.chat.id, "Price:"+price.text)


	if(message.text == "Market Cup"):
		bot.send_message(message.chat.id, "Market Cap: "+market_cup.text)


	if(message.text == "Value"):
		bot.send_message(message.chat.id, "Value: "+value.text)


	elif(message.text == "Back"):
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn1 = types.KeyboardButton("Bitcoin")
		btn2 = types.KeyboardButton("Ethereum")
		btn3 = types.KeyboardButton("BNB")
		btn4 = types.KeyboardButton("Dogecoin")
		markup.add(btn1, btn2, btn3, btn4)
		bot.send_message(message.chat.id, text="Choose option", reply_markup=markup)







bot.polling(none_stop=True)


