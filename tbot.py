from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_TOKEN' with your actual bot token
TOKEN = '6761392846:AAGVLI92-CuFcv9vdfDEpo6YFr061vQIWvo'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your bot. Type something, and I will respond with a hello.')

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello, blah blah... You said: ' + update.message.text)

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
