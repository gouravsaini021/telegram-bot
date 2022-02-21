from os import sep
import sqlite3
import question_set
from dataclasses import dataclass

from question_set import gk_paper, math_paper

def connect_db():
	global conn,cur
	conn=sqlite3.connect('test.db',check_same_thread=False)
	# conn=sqlite3.connect('test2.db',check_same_thread=False)

	cur=conn.cursor()

connect_db()

# def get_current_user_details(chat_id):
# 	cur.execute("")
def get_score(chat_id:int,paper_name:str):
	connect_db()
	ro=cur.execute("select correct_ans from user_history where chat_id=(?) and paper_name=(?)",(chat_id,paper_name))
	row=ro.fetchall()
	correct_ans=row[0][0]
	conn.close()
	return correct_ans
	
def set_current_paper(chat_id,current_paper):
	#------------------------
	connect_db()
	#---
	ro=cur.execute("select current_paper from current_detail where chat_id=(?)",(chat_id,))
	row=ro.fetchall()

	if len(row)==0:
		cur.execute("Insert into current_detail values(?,?)",(chat_id,current_paper))
		conn.commit()
	else:
		cur.execute('''update current_detail set current_paper=(?) where chat_id=(?)''',(current_paper,chat_id))
		conn.commit()
	#---
	ro=cur.execute("select question_no,correct_ans from user_history where chat_id=(?) and paper_name=(?)",(chat_id,current_paper))
	row=ro.fetchall()
	if len(row)==0:
		cur.execute("Insert into user_history values(?,?,?,?)",(chat_id,current_paper,0,0))
		conn.commit()
	else:
		with conn:
			conn.execute("update user_history set question_no=(?),correct_ans=(?) where chat_id=(?) and paper_name=(?)",(0,0,chat_id,current_paper))
	
	#---
	conn.close()
	#----------------------

def get_question_no_and_paper_name(chat_id):
	connect_db()
	ro=conn.execute("select current_paper from current_detail where chat_id=(?)",(chat_id,))
	row=ro.fetchall()
	paper_name=row[0][0]
	ro=conn.execute("select question_no from user_history where chat_id=(?) and paper_name=(?)",(chat_id,paper_name))
	row=ro.fetchall()
	question_no=row[0][0]
	conn.close()
	return question_no,paper_name


def get_question(question_no:int,paper_name:str):
	connect_db()
	ro=conn.execute("select paper_id from paper_details where paper_name=(?)",(paper_name,))
	row=ro.fetchall()
	paper_id=row[0][0]
	ro=conn.execute("select question from question_details where paper_id=(?) and question_no=(?)",(paper_id,question_no+1))
	row=ro.fetchall()
	question=row[0][0]
	conn.close()
	return question
def get_previous_answer_and_explantion(question_no:int,paper_name:str):
	connect_db()
	ro=conn.execute("select paper_id from paper_details where paper_name=(?)",(paper_name,))
	row=ro.fetchall()
	paper_id=row[0][0]
	ro=conn.execute("select answer,explanation from question_details where paper_id=(?) and question_no=(?)",(paper_id,question_no))
	row=ro.fetchall()
	answer=row[0][0]
	explanation=row[0][1]
	conn.close()
	return answer,explanation

def update_question_no(question_no:int,chat_id:int,paper_name:str):
	connect_db()
	cur.execute("update user_history set question_no=(?) where paper_name=(?) and chat_id=(?)",(question_no,paper_name,chat_id))
	conn.commit()
	conn.close()
def update_correct_ans(chat_id:int,paper_name:str):
	connect_db()
	ro=cur.execute("select correct_ans from user_history where chat_id=(?) and paper_name=(?)",(chat_id,paper_name))
	row=ro.fetchall()
	correct_ans=row[0][0]
	cur.execute("update user_history set correct_ans=(?) where paper_name=(?) and chat_id=(?)",(correct_ans+1,paper_name,chat_id))
	conn.commit()
	conn.close()

def maximum_question_no(paper_name):
	connect_db()
	ro=conn.execute("select paper_id from paper_details where paper_name=(?)",(paper_name,))
	row=ro.fetchall()
	paper_id=row[0][0]

	ro=conn.execute("select count(question_no) from question_details where paper_id=(?)",(paper_id,))
	row=ro.fetchall()
	conn.close()
	return row[0][0]

# --------------------------

def current():
	cur.execute('''create table current_detail(
		chat_id integer primary key not null,
		current_paper text not null)
		''')
# current()

def insert_current_details(chat_id,current_paper):
	data=(chat_id,current_paper)
	cur.execute("""Insert into current_details values(?,?)
		""",data)
	conn.commit()

def user_history():
	cur.execute('''create table user_history(
		chat_id integer not null,
		paper_name text not null,
		question_no integer not null,
		correct_ans integer not null)
		''')
	conn.commit()
# user_history()
def Insert_user_history(chat_id,paper_name,question_no=None,correct_ans=None):
	if question_no==None or correct_ans==None:
		data=(chat_id,paper_name,0,0)
	else:
		data=(chat_id,paper_name,question_no,correct_ans)
	cur.execute('''
		Insert into paper_details(paper_id,paper_name)
		values(?,?,?,?)''',data)
	conn.commit()

def fetch_user(user_id,paper_name):
	cur.execute("select question_no from user_history where user_id=(?) and paper_name=(?)")



def paper_details():
	cur.execute('''create table paper_details(
		paper_id integer primary key not null,
		paper_name text not null
		)
		''')


def question_details():
	cur.execute('''create table question_details(
		question_no integer not null,
		question text not null,
		answer integer not null,
		explanation text,
		paper_id not null,
		foreign key(paper_id) references paper_details(paper_id))''')

def insert_paper_details(paper_id,paper_name):
	data=(paper_id,paper_name)
	conn.commit()

def insert_question_details(data):
	d=[data.question_nu,data.question,data.answer,data.explanation,data.paper_id]
	cur.execute('''Insert into question_details
		values(?,?,?,?,?)''',d)
	conn.commit()

def create_tables():
	cur.executescript(open("init.sql").read())


if __name__ == "__main__":
	connect_db()
	create_tables()
	conn.commit()
	conn.close()

	question_details()
	x=math_paper()
	for i in x:
		insert_question_details(i)
	z=gk_paper()
	for i in z:
		insert_question_details(i)
