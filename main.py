import logging
from telegram.ext import *
#import responses
API_KEY="5174250209:AAG7fyel3thQD1FMIexJhjBKOPfBS8uea58"

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',level=logging.INFO)
logging.info('Starting bot...')

def start_command(update,context):
    print(update)
    update.message.reply_text('Hello thelkjlkjre!  I\'m a bot. What \'s up?')
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
USER_TAKING_GK_QUIZ = False

def handle_message(update,context):
    print(" USER taking", USER_TAKING_GK_QUIZ)

    if USER_TAKING_GK_QUIZ:
        print("stopped gk")
        #handle_gk(update, context)
        return
    print("update=",update,"context=",context)
    # print(type(update))
    text=str(update.message.text).lower()
    print(text)
    if text=="who is ankit":
        update.message.reply_text("Hitler")

    #Bot response
    else:
        update.message.reply_text(stext)
    logging.info(f'User({update.message.chat.id}) says: {text}')

def error(update,context):
    logging.error(f'Update{update} caused error {context.error}'  )

def handle_gk(update, context):
    print("In Handle Gk", update)
def mygk(update,context):
    global USER_TAKING_GK_QUIZ
    print("i am in gk function ")
    USER_TAKING_GK_QUIZ = True
    print("SET USER taking")
    dp.add_handler(MessageHandler(Filters.text, handle_gk))
    print(dp.handlers)


    

    


if __name__=='__main__':
    updater=Updater(API_KEY,use_context=True)
    dp=updater.dispatcher
    
    

    #commands
    dp.add_handler(CommandHandler('start',start_command))
    dp.add_handler(CommandHandler('help',help_command))
    dp.add_handler(CommandHandler('gk',mygk))
    #message
    dp.add_handler(MessageHandler(Filters.text,handle_message ))

    #Run the bot
    updater.start_polling(1.0)
    updater.idle() 
    
