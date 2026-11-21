import os
import telebot
from telebot import types

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = os.getenv("CHANNEL_ID")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "Привіт! 🎵 Напиши назву пісні або виконавця."
    )

@bot.message_handler(func=lambda message: True)
def search_music(message):
    query = message.text
    keyboard = types.InlineKeyboardMarkup()
    url = "https://www.youtube.com/results?search_query=" + query.replace(" ", "+")
    keyboard.add(types.InlineKeyboardButton(
        "Знайти пісню 🎵",
        url=url
    ))
    bot.reply_to(message, "Ось пошук твоєї пісні:", reply_markup=keyboard)
