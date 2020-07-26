import requests;
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters;
telegram_token = ''
g=''

def start(bot, update):
    update.message.reply_text('Привет')

def replay(bot, update):
    inp = str(update.message.text)
    text = '\n—' + inp + '\n—'
    params = {
        'length': 30,
        'num_samples': 1,
        'prompt': text,
    }
    response = requests.post('https://models.dobro.ai/gpt2/medium/', json=params)
    global g
    g=g + text + response.text[14:-3]
    print(g)
    update.message.reply_text(response.text[14:-3])
    if len(g)>500:
        g=''

updater = Updater(token=telegram_token)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, replay))

updater.start_polling()
updater.idle()