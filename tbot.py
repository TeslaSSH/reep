from telegram.ext import Updater, MessageHandler, Filters

def reply_hello(update, context):
    user_name = update.message.from_user.username
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hello, {user_name}!")

def main():
    # Replace 'YOUR_BOT_TOKEN' with the token obtained from BotFather
    updater = Updater(token='6761392846:AAGVLI92-CuFcv9vdfDEpo6YFr061vQIWvo', use_context=True)
    dp = updater.dispatcher

    # Register a handler to reply with 'Hello' to any incoming message
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_hello))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
