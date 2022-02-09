from dataclasses import dataclass, asdict
from logging import currentframe
from typing import Dict
from telegram.ext import *
import telegram
from queue import Queue
from collections import defaultdict

msg_queue = Queue()

API_KEY = "5174250209:AAG7fyel3thQD1FMIexJhjBKOPfBS8uea58"




@dataclass
class Question:
	question: str
	answer: int
	explanation: str

questions=[
	Question("who is next PM of India \n 1.narendra modi \t 2. amit shah ",1,"because amit shah has more power"),
	Question("How many hours in day \n 1. 24 \t 12",1,"24 horur in a day"),
	Question("what is more important for initial days \n 1. saving \t investment",1,"you always have saving for energency"),
	Question("which sport is more popular \n 1. cricket \t 2.badminton",1,"cricket is 2nd most popular sport than football")

]

@dataclass
class User:
	next_question: int =0
	correct_ans: int = 0

	def has_next_question(self) -> bool:
		return self.next_question != len(questions)

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
	chat_id=update.message.chat_id
	chat_message=update.message.text


	user = users[chat_id]

	
	if user.has_prev_question():
		prev_question = user.get_prev_question()
		if str(prev_question.answer) == chat_message:
			user.correct_ans += 1
			update.message.reply_text("Right Answer")
		else:
			update.message.reply_text("Wrong Answer")

		update.message.reply_text(prev_question.explanation)

	if user.has_next_question():
		curr_question = user.get_next_question()
		update.message.reply_text(curr_question.question)
	else:
		report = f"Your score is {user.correct_ans}/{len(questions)}"
		update.message.reply_text(report)





if __name__ == "__main__":
	updater = Updater(API_KEY, use_context=True)
	dp: Dispatcher = updater.dispatcher
	dp.add_handler(MessageHandler(Filters.text, my_handle_gk))
	updater.start_polling(1.0)
	# main()
