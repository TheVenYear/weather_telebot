import telebot
import settings

bot = telebot.TeleBot(settings.TELEGRAM_KEY, )


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, settings.HELLO_MESSAGE, parse_mode='markdown')
	img = open('./assets/hello.gif', 'rb')
	bot.send_animation(message.chat.id, img)


bot.polling()
