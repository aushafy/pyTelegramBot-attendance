import telebot
import datetime
import json
import os
from geopy import distance
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
    #timestamp = datetime.datetime.fromtimestamp(message.date)
    if verify_user(message.from_user.username) == True:
        keyboard = types.ReplyKeyboardMarkup(True)
        button_location = types.KeyboardButton(text="Share Location", request_location=True)
        keyboard.add(button_location)
        bot.send_message(message.chat.id, "Halo " + message.from_user.username.title() + "! \n\nUntuk melakukan absensi silahkan kirimkan lokasi Anda", reply_markup=keyboard)   
        #bot.send_message(chat_id=message.from_user.id, text="Terima kasih " + message.from_user.username.title() + "! \n\nAnda sudah melakukan check-in absensi pada tanggal dan waktu " + timestamp.strftime('%Y-%m-%d %H:%M:%S'))
    else:
        bot.send_message(chat_id=message.from_user.id, text="Maaf, Anda tidak terdaftar sebagai karyawan di perusahaan kami.")

@bot.message_handler(commands=['checkout'])
def checkout(message):
    timestamp = datetime.datetime.fromtimestamp(message.date)
    if verify_user(message.from_user.username) == True:
        bot.send_message(chat_id=message.from_user.id, text="Terima kasih " + message.from_user.username.title() + "! \n\nAnda sudah melakukan check-out absensi pada tanggal dan waktu " + timestamp.strftime('%Y-%m-%d %H:%M:%S'))
    else:
        bot.send_message(chat_id=message.from_user.id, text="Maaf, Anda tidak terdaftar sebagai karyawan di perusahaan kami.")

@bot.message_handler(content_types=['location'])
def check_loc(message):
    latitude = message.location.latitude
    longitude = message.location.longitude

    geoloc_office = (-6.1751097596994375, 106.81438541338262) # -6.1751097596994375, 106.81438541338262
    geoloc_user = (latitude, longitude) 

    distance_calc = distance.distance(geoloc_office, geoloc_user).kilometers

    if distance_calc <= float(1.0000000000):
        bot.send_message(chat_id=message.from_user.id, text="Verified absen anda diterima")
    else:
        bot.send_message(chat_id=message.from_user.id, text="Unverified! lokasi anda terlalu jauh dari kantor")

bot.polling()