
import Constans as keys
from telegram.ext import *
import Responses as R

print("bot başladı......")

def start_command(update, context):
    update.message.reply_text('agfsasf')
def help_command(update, context):
    update.message.reply_text('arif')
def handle_message(update, context):
    text = str(update.message.text).lower()
    respose = R.sample_resposes(text)
def job_jobs(update, context):
    text = str(update.message.text).lower()
    respose=R.ar_resposes(text)

    update.message.reply_text(respose)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp=updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("start", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()