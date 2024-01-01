from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from pytube import YouTube
import validators  # Install it with: pip install validators

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

        # Check if the URL is valid
        if not validators.url(video_url):
            raise ValueError('Invalid URL')

        # Downloading the video
        youtube = YouTube(video_url)
        video = youtube.streams.get_highest_resolution()
        video_file_path = f'{video.title}.mp4'
        video.download(filename=video_file_path)

        # Send the video file to the chat
        context.bot.send_video(chat_id=chat_id, video=open(video_file_path, 'rb'), supports_streaming=True)

        update.message.reply_text('Video sent successfully!')

    except Exception as e:
        update.message.reply_text(f'Error processing the video: {str(e)}. Make sure the URL is valid and try again.')

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
