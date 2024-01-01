from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from pytube import YouTube

# Replace 'YOUR_TOKEN' with your actual bot token
TOKEN = '6761392846:AAGkAIOuBLcqFXQUN5EUT8qWT4SP2qW8RTA'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your bot. Type /help to see available commands.')

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('You can use the /download command to download YouTube videos. Just send the video URL after the command.')

def download(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    text = update.message.text
    try:
        # Extracting video URL from the command
        video_url = text.split(' ', 1)[1]

        # Downloading the video
        youtube = YouTube(video_url)
        video = youtube.streams.get_highest_resolution()
        video.download()

        update.message.reply_text('Video downloaded successfully!')

    except Exception as e:
        update.message.reply_text('Error downloading the video. Make sure the URL is valid and try again.')

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("download", download))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
