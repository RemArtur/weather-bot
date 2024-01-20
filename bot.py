import telebot
import requests
from configuration.config import bot_token, weather_api_key
import json

bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, напиши мне название города и я покажу погоду.')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    weather = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?q={message.text}&units=metric&lang=ru&appid={weather_api_key}'
    )
    print(weather.text)
    json_weather = json.loads(weather.text)
    bot.send_message(message.chat.id, f'Температура в городе {message.text} {json_weather["main"]["temp"]} °C')

bot.polling(none_stop=True)
