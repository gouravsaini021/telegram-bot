import os
import database
from typing import *
from telegram.ext import *
import telegram
import json

from question_set import question_set


API_KEY = os.environ.get('telegram_token')
print(API_KEY)

def start(update,_):
	update.message.reply_text("type /gk or /math for gk or math paper recpectively")
def gk(update,_):
	chat_id=update.message.chat_id
	update.message.reply_text("""Instruction Guideliness""")
	database.set_current_paper(chat_id,"gk")
def math(update,_):
	chat_id=update.message.chat_id
	update.message.reply_text("""Instruction Guideliness""")
	database.set_current_paper(chat_id,"math")

def my_handle_response(update,_):
	chat_id=update.message.chat_id
	chat_message=update.message.text
	question_no,paper_name=database.get_question_no_and_paper_name(chat_id)

	maximum_question_no=database.maximum_question_no(paper_name)
	if question_no==0:
		question=database.get_question(question_no,paper_name)
		update.message.reply_text(question)
		database.update_question_no(question_no+1,chat_id,paper_name)
	elif question_no<maximum_question_no+1 and question_no!=0:
		answer,explanation=database.get_previous_answer_and_explantion(question_no,paper_name)
		if chat_message==str(answer):
			update.message.reply_text("Right Answer")
			database.update_correct_ans(chat_id,paper_name)
		else:
			update.message.reply_text("Wrong Answer")
		update.message.reply_text(explanation)
	if question_no<maximum_question_no and question_no!=0:
		question=database.get_question(question_no,paper_name)
		database.update_question_no(question_no+1,chat_id,paper_name)
		update.message.reply_text(question)
	elif question_no==maximum_question_no:
		score=database.get_score(chat_id,paper_name)
		database.update_question_no(question_no+1,chat_id,paper_name)
		update.message.reply_text("your result is "+str(score)+" out of "+str(maximum_question_no))


	
if __name__ == "__main__":

	database.create_tables()


	updater = Updater(API_KEY, use_context=True)
	dp: Dispatcher = updater.dispatcher
	dp.add_handler(CommandHandler('start',start))
	dp.add_handler(CommandHandler('gk',gk))
	dp.add_handler(CommandHandler('math',math))
	dp.add_handler(MessageHandler(Filters.text, my_handle_response))
	
	updater.start_polling(1.0)
	updater.idle()
