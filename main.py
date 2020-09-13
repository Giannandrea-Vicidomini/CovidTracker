from utils.DataManager import QueryManager;
import json;
from telegram.ext import Updater, CommandHandler
import logging
import telegram
import requests
import os
from dotenv import load_dotenv;


#logger config
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)


def main():
    load_dotenv();
    manager = QueryManager(os)

    # INITIALISES UPDATER TO GET THE BOT FUNCTIONALITY
    updater = Updater(token=os.environ.get("TOKEN"), use_context=True)
    dp = updater.dispatcher

    #INITIALISES LIST OF COMMANDS
    initialiseCommands(dp);

    #STARTS POLLING WAITING FOR MESSAGES
    updater.start_polling()
    updater.idle()



def initialiseCommands(dp):
    startHandler = CommandHandler("start",start);
    dp.add_handler(startHandler)



#BOT COMMANDS
def start(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi there!")




if __name__ == "__main__":
    main()
