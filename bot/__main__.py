from . import bot
from handlers import handle
if __name__=='__main__':
    bot.register_message_handler(handle.message_handl,pass_bot=True)
    bot.infinity_polling()