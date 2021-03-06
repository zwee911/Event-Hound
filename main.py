import os
from flask import Flask
from telegram.ext import Updater, CommandHandler, CallbackContext


app = Flask(__name__)
TOKEN = '1253905644:AAG3ma_w8ILDd4QHsPYSvxf3FZvN1YJyc0c'
el_cine_id = '-235237146'

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def callback_trump(context: CallbackContext):
    context.bot.send_message(chat_id=el_cine_id, text='trump 2020')

@app.route('/')
def hello_world():
    name = os.environ.get('NAME', 'World')
    return 'Hello {}!'.format(name)

if __name__ == "__main__":
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    updater.start_polling()

    job_q =  updater.job_queue
    job_q.run_repeating(callback_trump, interval=10, first=0)

    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
