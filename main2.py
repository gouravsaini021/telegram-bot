import os
from dataclasses import dataclass, asdict
from logging import currentframe
from typing import Dict
from telegram.ext import *
import telegram
from queue import Queue
from collections import defaultdict
import json

msg_queue = Queue()

API_KEY =os.environ.get('telegram_token')


questions=None

@dataclass
class Question:
	question: str
	answer: int
	explanation: str
def mathquestion(update,_):
	global questions
	questions=[
		Question("2+2=? \n 1). 4 \t 2). 5 \n 3). 8 \t 4). 0 ",1,"2+2 is 4"),
		Question("What is the value of pi? \n 1). 3.14  \t2). 3.33 \n 3). 99 \t 4). 7/22",1,"The value of pi is 3.14"),
		Question("What is the area of square \n 1). side+side \t2). side-side \n 3). side*side \t 4). side/side",3,"The area of square is side*side"),
		Question("What is the area of rectangle \n 1). length+breadth  \t 2). length*breadth \n 3). length-breadth \t 4). length//breadth",2,"The area of rectangle is length*breadth")

	]
def gkquestion(update,_):
	# print("hello")
	global questions
	questions=[
		Question("Who invented Computer? \n 1.charles babbage \t 2. Albert Einstein \n 3.Newton \t 4.Rahul Gandhi ",1,"Charles Babbage is Father of Computer"),
		Question("1024 Kilobytes is equal to? \n 1). 1 GB \t2). 1 MB \n 3). 1 TB \t 4). 1 BB",2,"1024 Kilobytes(KB) =1 Mega Bytes(MB)"),
		Question("How many players are there in a cricket team? \n 1). 12 \t2). 15 \n 3). 11 \t 4). 22",3,"cricket has 11 players"),
		Question(" Who was the inventor of the light bulb? \n 1. Thomas Edison \t 2.Albert Einstein \n 3. Andrew ng \t 4. Arwind kejriwal",1,"Thomas Edison invented bulb")

	]

def fetch_data():
	with open('file.txt','r') as f:
		x=json.load(f)
	return x
def update_data(mydata_dict,chat_id,question=None,correct_ans=None):

	# print("question=",question)
	if question ==None:
		mydata_dict[chat_id]['correct_ans']=correct_ans
	if correct_ans ==None:
		mydata_dict[chat_id]['question_no']=question
	
	# print("dict:", mydata_dict[chat_id])

def insert_data(js):
	with open ('file.txt','w') as f:
		json.dump(js,f)
@dataclass
class User:
	next_question: int =0
	correct_ans: int = 0

	def has_next_question(self) -> bool:
		return self.next_question < len(questions)

	def has_prev_question(self) -> bool:
		return self.next_question != 0
	
	def get_next_question(self) -> Question:
		question = questions[self.next_question]
		self.next_question += 1
		return question

	def get_prev_question(self) -> Question:
		return questions[self.next_question-1]

# asdict(User(next_question=3))  -> {'next_question':3, 'correct_ans': 0}
users: Dict[str, User] = defaultdict(User)


def my_handle_gk(update, _):
	if questions==None:
		update.message.reply_text("type /gk or /math for gk and math questions recpectively")
	else:
		chat_id=update.message.chat_id
		chat_id=str(chat_id)
		chat_message=update.message.text
		mydata_dict=fetch_data()
		
		if chat_id not in mydata_dict or mydata_dict[chat_id]['question_no']>len(questions):
			mydata_dict[chat_id]={'question_no':0,'correct_ans':0}
			
		question_nu=mydata_dict[chat_id]['question_no']
		correct_ans=mydata_dict[chat_id]['correct_ans']

		if question_nu<=len(questions):
			if question_nu<len(questions):
				question=questions[question_nu].question
			answer=questions[question_nu-1].answer
			explanation=questions[question_nu-1].explanation
		user = users[chat_id]
		# print(user,type(user))
		# print(mydata_dict[chat_id])
		if question_nu==0:
			update.message.reply_text(question)
			update_data(mydata_dict,chat_id,question=question_nu+1)
			# print(mydata_dict)
		elif question_nu<len(questions)+1 and question_nu!=0:
			if chat_message==str(answer):
				update_data(mydata_dict,chat_id,correct_ans=correct_ans+1)
				update.message.reply_text("Right Answer")
			else:
				update.message.reply_text("Wrong Answer")
				# update_data(mydata_dict,chat_id,correct_ans=correct_ans)
			update.message.reply_text(explanation)
			if question_nu<len(questions):
				update.message.reply_text(question)
			else:
				correct_ans=mydata_dict[chat_id]['correct_ans']
				update.message.reply_text("your score is "+str(correct_ans)+" /"+str(len(questions)))
			update_data(mydata_dict,chat_id,question=question_nu+1)
		else:
			update_data(mydata_dict,chat_id,question=question_nu+1)
		print(mydata_dict)
		insert_data(mydata_dict)

	# if user.has_prev_question() and user.next_question!=len(questions)-1:
	# 	prev_question = user.get_prev_question()
	# 	if str(prev_question.answer) == chat_message:
	# 		user.correct_ans += 1
	# 		update.message.reply_text("Right Answer")
	# 	else:
	# 		update.message.reply_text("Wrong Answer")

	# 	update.message.reply_text(prev_question.explanation)


	# if user.has_next_question():
	# 	curr_question = user.get_next_question()
	# 	update.message.reply_text(curr_question.question)
	# else :
	# 	report = f"Your score is {user.correct_ans}/{len(questions)}"
	# 	update.message.reply_text(report)





if __name__ == "__main__":
	updater = Updater(API_KEY, use_context=True)
	dp: Dispatcher = updater.dispatcher
	dp.add_handler(CommandHandler('gk',gkquestion))
	dp.add_handler(CommandHandler('math',mathquestion))
	dp.add_handler(MessageHandler(Filters.text, my_handle_gk))
	
	updater.start_polling(1.0)
	updater.idle()
	# main()
