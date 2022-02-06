import telebot
import os
import sys
import time
from loguru import logger


class Telechat:
    def __init__(self):
        # self.token = os.environ['teletoken']
        self.bot = telebot.TeleBot(os.environ['TELETOKEN'], parse_mode=None)
        self.start()
        logger.info("Starting bot")
        

    def start(self):
        logger.info("some info")
        
        @self.bot.message_handler(commands=['start', 'help'])
        def send_welcome(message):
            self.bot.reply_to(message, 'Howdy, how are you doing?')


        @self.bot.message_handler(func=lambda m: True)
        def echo_all(message):
            self.bot.reply_to(message, message.text)
        
        self.bot.infinity_polling()

    # def run(self):
    #     self.bot.infinity_polling()


if __name__ == '__main__':
    chat = Telechat()