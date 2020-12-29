import telebot
import datetime
import json
import os
from telebot import types

bot = telebot.TeleBot(str(os.environ['TOKEN']))

def verify_user(username):
    with open("user.json", "r") as user_file:
        data = user_file.read()

    data_json = json.loads(data)
    if username in data_json["username"]:
        return True
    else:
        return False

@bot.message_handler(commands=['checkin'])
def checkin(message):
    timestamp = datetime.datetime.fromtimestamp(message.date)
    if verify_user(message.from_user.username) == True:
        bot.send_message(chat_id=message.from_user.id, text="Terima kasih " + message.from_user.username.title() + "! \n\nAnda sudah melakukan check-in absensi pada tanggal dan waktu " + timestamp.strftime('%Y-%m-%d %H:%M:%S'))
    else:
        bot.send_message(chat_id=message.from_user.id, text="Maaf, anda tidak terdaftar pada database perusahaan kita")

@bot.message_handler(commands=['checkout'])
def checkout(message):
    timestamp = datetime.datetime.fromtimestamp(message.date)
    if verify_user(message.from_user.username) == True:
        bot.send_message(chat_id=message.from_user.id, text="Terima kasih " + message.from_user.username.title() + "! \n\nAnda sudah melakukan check-out absensi pada tanggal dan waktu " + timestamp.strftime('%Y-%m-%d %H:%M:%S'))
    else:
        bot.send_message(chat_id=message.from_user.id, text="Maaf, anda tidak terdaftar pada database perusahaan kita")

bot.polling()