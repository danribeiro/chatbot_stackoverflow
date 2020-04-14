from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, Filters
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
