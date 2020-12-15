import telebot
import settings
from weather_api import OpenWeather

bot = telebot.TeleBot(settings.TELEGRAM_KEY, )
weather = OpenWeather(settings.OPEN_WEATHER_KEY)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, settings.HELLO_MESSAGE, parse_mode='html')
    img = open('./assets/hello.gif', 'rb')
    bot.send_animation(message.chat.id, img)


@bot.message_handler(content_types=['text'])
def weather_handler(message):
    if message.text.lower() in settings.HELLO_ARRAY:
        bot.send_message(message.chat.id, 'Привет, друг :)')

    else:
        try:
            data = weather.get_weather(message.text)
            bot.send_message(message.chat.id,
                             f'Название города: {data["name"]}\n'
                             f'Температура: {data["temp"]}\n'
                             f'Ощущается как: {data["feels_like"]}\n'
                             f'Погода: {data["description"]}'
                             )

        except Exception as err:
            bot.send_message(message.chat.id, err)

print('Bot has been started successfully')
bot.polling()

