import logging
from telegram.ext import *
#import responses
API_KEY="5174250209:AAG7fyel3thQD1FMIexJhjBKOPfBS8uea58"

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',level=logging.INFO)
logging.info('Starting bot...')

def start_command(update,context):
    update.message.reply_text('Hello there! I\'m a bot. What \'s up?')
    update.message.reply_text('who is pm of india /n 1.narendra modi/t 2.manhoman singh')
    text=str(update.message.text).lower()
    print(text)

    if text=="1":
        update.message.reply_text('Right answer')
    else:
        update.message.reply_text('wrong answer narendra modi is prime minister of india')
        

def help_command(update,context):
    update.message.reply_text('try typing anything and i will do my best to respond!')

def custom_command(update,context):
    update.message.reply_text('This a custom command')



def handle_message(update,context):
    text=str(update.message.text).lower()
    
    if text=="who is ankit":
        update.message.reply_text("Hitler")

    #Bot response
    else:
        update.message.reply_text(text)
    logging.info(f'User({update.message.chat.id}) says: {text}')

def error(update,context):
    logging.error(f'Update{update} caused error {context.error}'  )

def mygk(update,context):
    print("hello")

if __name__=='__main__':
    updater=Updater(API_KEY,use_context=True)
    dp=updater.dispatcher

    
    #commands
    dp.add_handler(CommandHandler('start',start_command))
    dp.add_handler(CommandHandler('help',help_command))

    #message
    dp.add_handler(MessageHandler(Filters.text,handle_message ))

    #Run the bot
    updater.start_polling(1.0)
    updater.idle() 
    
