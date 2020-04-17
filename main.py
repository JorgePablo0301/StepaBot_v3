import telebot
import discogs_client_findprice

API_TOKEN = '1106213214:AAH6K0eg-wIwmqHjKKaOLlX0wPVEHSEKwj0'

bot = telebot.TeleBot(API_TOKEN)

dcfindprice = discogs_client_findprice.DcFindPrice()


@bot.message_handler(commands=['start'])
def start(message):
    send_mess = "Пивееет"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')

@bot.message_handler(commands=['artist'])
def text_req(message):
    send_mess = "Назовите пожлуйста артиста"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')

@bot.message_handler(commands=['help'])
def text_req(message):
    send_mess = '''
                /artist - Имя артиста
                A: - Имя артиста
                /year - Год
                Y: - Год
                /album - Альбом                
                text - поиск
                '''
    bot.send_message(message.chat.id, send_mess, parse_mode='html')

@bot.message_handler(content_types=['text'])
def text_req(message):
    send_mess = "Пивееет111"
    #bot.send_message(message.chat.id, send_mess, parse_mode='html')

    dcfindprice.var_name = 'Queen Sheer Heart Attack us'
    #dcfindprice.printdata = "3"
    # dcfindprice.PRINT_RESULT = 1
    dcfindprice.main_find()
    dcfindprice.main_findprint()
    print(dcfindprice.print_data)
    send_mess = dcfindprice.title
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
#$ git push heroku master