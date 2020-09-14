from utils.CovidData import CovidData
import telebot
import dotenv
import os
import logging
import re
import json
#logger config
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

#LOADING DOTENV FILE
dotenv.load_dotenv();
manager = CovidData(os)
regions = manager.getRegionList()
regions.insert(0,"Nazione")

########## SETUP ############
def create_keyboard():
    keyboard = [telebot.types.KeyboardButton(text=label) for label in regions]

    markup = telebot.types.ReplyKeyboardMarkup().add(*keyboard)
    return markup




################## BOT ####################
bot = telebot.TeleBot(os.environ.get("TOKEN"))
markup = create_keyboard()
regex = "^[cC][eE][nN][cC][iI][oO]$"



@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id,"Hi there, choose the region you want to see the data of by typing /regions")

@bot.message_handler(commands=["regions"])
def show_keyboard(message):
    bot.send_message(message.chat.id,"Choose a region:",reply_markup = markup)


@bot.message_handler(func=lambda message: True if message.text in regions else False)
def show_data(message):

    string = ""

    if (message.text == "Nazione"):
        data = manager.getNationalStatus()[0]

        string = "Nation: Italia\n" \
                 f"deaths: {data['deceduti']}\n" \
                 f"healed people: {data['dimessi_guariti']}\n" \
                 f"positives: {data['totale_positivi']}"
    else:
        data = manager.getRegionStatus(message.text)

        string = f"Region: {message.text}\n" \
                 f"deaths: {data['deceduti']}\n" \
                 f"healed people: {data['dimessi_guariti']}\n" \
                 f"positives: {data['totale_positivi']}"

    bot.send_message(message.chat.id,string)

@bot.message_handler(func = lambda message: re.match(regex,message.text))
def insult_cencio(message):
    bot.send_message(message.chat.id,"Nadda mai fa ben nda vit chillu merd...")


bot.polling(none_stop=False)