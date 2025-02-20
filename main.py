from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Bot is in deployment process. Kindly wait, it will take a couple of times.")

def main():
    TOKEN = "7081112444:AAF4K7peYIJoO8TT9Gxam-bJvYjgIb_R0bc"
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
