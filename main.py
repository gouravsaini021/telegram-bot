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
    
"""
PrivateBin
    
 This document will expire in 5 days.
from dataclasses import dataclass
from telegram.ext import *
import telegram
from queue import Queue

msg_queue = Queue()

API_KEY = "5174250209:AAG7fyel3thQD1FMIexJhjBKOPfBS8uea58"

QUESTION_NO = 0


@dataclass
class Question:
    question: str
    answer: int
    explanation: str


def main():
    bot = updater.bot
    questions = [
        Question("Who is ankit? 1: great man 2: hitler", 1, "Not a hitler"),
        Question("Who is gourav? 1: great man 2: hitler", 2, "Yes a hitler"),
    ]
    for i in range(100):
        questions.append(Question(f"Who is {i}? 1: great man 2: hitler", 2, "Yes a hitler"))


    user_msg, chat_id = msg_queue.get()

    for question in questions:
        bot.send_message(chat_id, question.question)
        user_msg, chat_id = msg_queue.get()
        if user_msg == str(question.answer):
            bot.send_message(chat_id, "Very good")
        else:
            bot.send_message(chat_id, "Wrong Answer. correct answer is " + str(question.answer))
            bot.send_message(chat_id, "Explanation: " + question.explanation)


def my_handle_gk(update, context):
    msg_queue.put((update.message.text, update.message.chat_id))


if __name__ == "__main__":
    updater = Updater(API_KEY, use_context=True)
    dp: Dispatcher = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, my_handle_gk))
    updater.start_polling(1.0)
    main()"""
