from email.errors import CharsetError
import telebot
import os
import sys
import time
from loguru import logger
from src.Utils.alarm import time_alarm

class Telechat:
    def __init__(self):
        # self.token = os.environ['teletoken']
        self.bot = telebot.TeleBot(os.environ['TELEBOT'], parse_mode=None)
        self.start()



    def start(self):
        logger.info("some info")

        @self.bot.message_handler(commands=["start", "help"])
        def send_welcome(message):
            self.bot.reply_to(message, "Howdy, how are you doing?")


        @self.bot.message_handler(commands=["time"])
        def time(message):
            self.bot.send_message(message.chat.id , time_alarm())

        self.bot.infinity_polling()

    def run(self):
        self.bot.infinity_polling()


if __name__ == '__main__':
    chat = Telechat()
    chat.run()