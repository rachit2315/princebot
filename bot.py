import os
from telegram.ext import Application, CommandHandler
from telegram import Update
from telegram.ext import ContextTypes

# Required package version: python-telegram-bot>=20.0

# Bot token directly in the file
BOT_TOKEN = "7081112444:AAF4K7peYIJoO8TT9Gxam-bJvYjgIb_R0bc"

# Define the start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.reply_text(
            "Bot is in deployment process. Kindly wait, it will take a couple of times."
        )
    except Exception as e:
        print(f"Error in start command: {str(e)}")
        await update.message.reply_text(
            "Sorry, there was an error processing your request."
        )

# Main function to run the bot
def main():
    try:
        # Create the Application and pass it your bot's token
        application = Application.builder().token(BOT_TOKEN).build()

        # Add command handler for /start
        application.add_handler(CommandHandler("start", start))

        # Start the bot
        print("Bot is starting...")
        application.run_polling(allowed_updates=Update.ALL_TYPES)

    except Exception as e:
        print(f"Error starting bot: {str(e)}")

if __name__ == '__main__':
    main()
