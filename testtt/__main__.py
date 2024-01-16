from TeleGenic.ext import Command

from testtt import komi , updater
from TeleGenic import Update
from TeleGenic.ext import CallbackContext , MessageHandler , Filters

def start(update : Update , context : CallbackContext) ->str :
    update.message.reply_text("komi")
    bot = context.bot
    chat_id = update.effective_chat.id
    bot.sendMessage(chat_id = chat_id , text = "hello")



def main():
    komi.add_handler(Command('start',start))

    updater.start_polling(timeout=15, read_latency=4, drop_pending_updates=True)
    updater.idle()

if __name__ == "__main__":
    main()