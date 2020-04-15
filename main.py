import telebot

API_TOKEN = '1106213214:AAH6K0eg-wIwmqHjKKaOLlX0wPVEHSEKwj0'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    send_mess = "Пивееет333"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')

@bot.message_handler(content_types=['text'])
def text_req(message):
    send_mess = "Пивееет111"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')


bot.polling(none_stop=True)

#If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.
#$ heroku login
#Clone the repository
#Use Git to clone stepabot3's source code to your local machine.
#$ heroku git:clone -a stepabot3
#$ cd stepabot3
#Deploy your changes
#Make some changes to the code you just cloned and deploy them to Heroku using Git.
#$ git add .
#$ git commit -am "make it better"
#$ git push heroku master

#$ git commit -am "make it better"
#$ heroku git:clone -a stepabot3
#$ heroku ps:scale web=1