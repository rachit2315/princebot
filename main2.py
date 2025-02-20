from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    update.message.reply_text("Bot is in deployment process. Kindly wait, it will take a couple of times.")

def main() -> None:
    TOKEN = 'YOUR_BOT_TOKEN'

    # Use the new Application class
    application = Application.builder().token(TOKEN).build()

    # Add a command handler to respond to /start
    application.add_handler(CommandHandler("start", start))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
