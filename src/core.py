import requests
import json
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from conf.settings import TELEGRAM_TOKEN


def start(bot, update):
    response_message = "Olá, digite os termos da pesquisa"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


def http_cats(bot, update, args):
    bot.sendPhoto(
        chat_id=update.message.chat_id,
        photo=BASE_API_URL + args[0]
    )


def call_stackoverflow_api(bot, update):

    splited_message = update.message.text.split(" ")
    tags = ";".join(splited_message)
    url = 'https://api.stackexchange.com/2.2/search/advanced?order=desc&sort=activity&tagged='+tags+'&site=stackoverflow'
    result_search = requests.get(url)
    result_json = result_search.content.decode('utf8').replace("'", '"')
    data = json.loads(result_json)

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

def main():
    updater = Updater(token=TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        CommandHandler('start', start)
    )

    dispatcher.add_handler(
        MessageHandler(Filters.text, call_stackoverflow_api)
    )

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()