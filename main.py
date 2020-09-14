from utils.CovidData import CovidData;
import json;
from telegram.ext import Updater, CommandHandler,CallbackQueryHandler
import logging
from telegram import KeyboardButton,ReplyKeyboardMarkup
import requests
import os
from dotenv import load_dotenv;
import types

#logger config
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

#LOADING DOTENV FILE
load_dotenv();
manager = CovidData(os)


def main():


    # INITIALISES UPDATER TO GET THE BOT FUNCTIONALITY
    updater = Updater(token=os.environ.get("TOKEN"), use_context=True)
    dp = updater.dispatcher

    #INITIALISES LIST OF COMMANDS
    initialiseCommands(dp);

    #STARTS POLLING WAITING FOR MESSAGES
    updater.start_polling()
    updater.idle()



def initialiseCommands(dp):
    startHandler = CommandHandler("start",menu);
    dp.add_handler(startHandler)
    helpHandler = CommandHandler("help",help)
    dp.add_handler(helpHandler)



#BOT COMMANDS ###########################
def start(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi there!")

def help(update,context):
    update.message.reply_text("use /start to use this bot")
##########################################

#MENU INITIALISATION#################################
def menu(update, context):
    keyboard = [[KeyboardButton("Option 1", callback_data='1'),
                 KeyboardButton("Option 2", callback_data='2')],

                [KeyboardButton("Option 3", callback_data='3')]]

    reply_markup = ReplyKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)
##################################################


if __name__ == "__main__":
    main()
