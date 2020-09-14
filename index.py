from utils.CovidData import CovidData
import telebot
import dotenv
import os
import logging

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


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id,"Hi there, choose the region you want to see the data of by typing /regions")

@bot.message_handler(commands=["regions"])
def show_keyboard(message):
    bot.send_message(message.chat.id,"Choose a region:",reply_markup = markup)

def check_input(message):
    if message.text in regions:
        return True
    else:
        return False

@bot.message_handler(func=check_input())
def show_data(message):
    bot.send_message(message.chat.id,"gni")

bot.polling(none_stop=False)