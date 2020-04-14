import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/Users/danilosoares/Documents/projetos/brasilprev/bpchatbot/src/')

from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, Filters

from utils import call_stackoverflow_api
from core import BotApi


class TestController(BotApi):
    def __init__(self, dispatcher):
        self.dispatcher = dispatcher
        self.__process_handlers()

    def __process_handlers(self):
        conversation_handler = ConversationHandler(
            entry_points=[CommandHandler("search", self.search_tags, pass_args=True)],
            states={}, 
            fallbacks=[], 
            allow_reentry=True
        )
        self.dispatcher.add_handler(conversation_handler)
