# Telegram Attendance Bot
Bot ini ditulis dengan menggunakan Python dengan dukungan library pyTelegramBotAPI ❤

Anda bisa melakukan tes bot ini pada akun Official Telegram Attendance Bot:
[@Callmea_bot](https://telegram.me/Callmea_bot)

Powered by [Aushafy](https://github.com/aushafy) ❤

# Instalasi

Prasyarat:
1. Python3
2. Pip3 package manager

Setelah semua prasyarat terpenuhi, selanjutnya Anda dapat men-download library pyTelegramBotAPI

```
sudo pip3 install pyTelegramBotAPI
sudo pip3 install geopy
```

Terakhir, lakukan kloning repository github

```
git clone https://github.com/aushafy/pyTelegramBot-attendance.git
```

# Konfigurasi

Sebelum menjalankan Bot, ada beberapa konfigurasi yang perlu Anda lakukan

1. Ekspor API Token

```
export TOKEN=TOKEN_API_ANDA
```
API Token ini bisa Anda dapatkan dari BotFather

2. Konfig user.json file

```
{
    "username": ["USERNAME_ANDA"] 
}
```

user.json file digunakan untuk menyimpan informasi username dari user yang diperbolehkan melakukan absensi, buka file user.json dan lakukan perubahan sesuai dengan username dari user yang akan menggunakan Attendance Bot.

# Jalankan Bot

Untuk dapat menjalankan bot, jalankan perintah berikut
```
python3 bot.py
```

# Testing

Bot ini dapat menerima beberapa perintah:
1. ```/checkin``` - untuk melakukan absensi masuk user
2. ```/checkout``` - untuk melakukan absensi keluar user
