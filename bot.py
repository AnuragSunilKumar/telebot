
import telebot
from flask import Flask, request
import os

TOKEN = "1761809933:AAGD4RFzRtecd0gL_RYJ8IVr7soNbVzgZ60"
bot = telebot.TeleBot(token=TOKEN)
server = Flask(__name__)



@bot.message_handler(commands=['start']) # welcome message handler
def send_welcome(message):
    bot.reply_to(message, 'Welcome')

@bot.message_handler(commands=['help']) # help message handler
def send_welcome(message):
    bot.reply_to(message, 'Type in a number and send it to me.I will send you a link which will open WhatsApp')

@bot.message_handler(func=lambda msg: msg.text is not None)

def at_converter(message):
    texts = int(message.text)
    
    if texts == int: 
        insta_link = "http://api.whatsapp.com/send?phone={}".format(texts)
        bot.reply_to(message, insta_link)
    else:
        pass
        

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://arcane-crag-50077.herokuapp.com/' + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))