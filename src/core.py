import requests
import json
from telegram.ext import CommandHandler, Updater
from telegram.base import TelegramObject
from utils import call_stackoverflow_api

TELEGRAM_TOKEN = '1083420625:AAHE1yozVMr8gCQcgI0jBDspucc8zxaDpLc'

class BotApi:
    @staticmethod
    def search_tags(bot, update, args):

        tags = ";".join(args)
        data = call_stackoverflow_api(tags)

        response_message = 'Nenhum resultado encontrado'

        if data['items'].__len__() > 0:
            for item in data['items']:
                response_message = "Question: {0}\n\nScore: {1}\n\nLink: {2}\n\n".format(item['title'], item['score'], item['link'])
                bot.send_message(
                    chat_id=update.message.chat_id,
                    text=response_message
                )
        else:
            bot.send_message(
                chat_id=update.message.chat_id,
                text=response_message
            )
        return data

def main():
    updater = Updater(token=TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('search', BotApi.search_tags, pass_args=True))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()