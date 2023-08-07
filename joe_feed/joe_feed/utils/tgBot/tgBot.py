import schedule
import time, os


from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

from joe_feed.utils.telegra.telegra import get_updates

# Replace 'YOUR_TOKEN' with your actual bot token
TOKEN = os.environ['Tsidin']

# def send_message(update: Update, context: CallbackContext):
#     chat_id = update.message.chat_id
#     context.bot.send_message(chat_id=chat_id, text='Hello, this is a repeated message!')

def send2chat(chat_id, sendWord):
    updater = Updater(TOKEN, use_context=True)
    # print("bot created")
    # Replace 'YOUR_CHAT_ID' with the chat ID you want to send the message to
    # chat_id = -1001849856114
    # ts = get_updates()
    # for t in ts:
        # print(t)
    # t = "test"
    updater.bot.send_message(chat_id=chat_id, text=sendWord)
        # time.sleep(1)

def main():
    print("start")
    # Get the job running every 5 seconds (adjust the interval as needed)
    # schedule.every(2).minutes.do(job)

    # Uncomment the following lines if you want to use a command to send a message
    # updater.dispatcher.add_handler(CommandHandler('send_message', send_message))

    # job()
    # while True:
        # schedule.run_pending()
        # time.sleep(1)
    # updater.start_polling()
    # updater.idle()

if __name__ == '__main__':
    main()
