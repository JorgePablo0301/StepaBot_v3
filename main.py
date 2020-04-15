import telebot

API_TOKEN = '1106213214:AAH6K0eg-wIwmqHjKKaOLlX0wPVEHSEKwj0'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    send_mess = "Пивееет"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')


@bot.message_handler(commands=['text'])
def text_req(message):
    send_mess = "Пивееет111"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')


bot.polling(none_stop=True)