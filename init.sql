create table if not exists user_history(
	chat_id integer,
	paper_name text,
	question_no integer,
	correct_ans integer
);


create table if not exists current_detail(
	chat_id integer primary key not null,
	current_paper text not null);

create table if not exists paper_details(
	paper_id integer primary key not null,
	paper_name text not null
);

create table if not exists question_details(
	question_no integer not null,
	question text not null,
	answer integer not null,
	explanation text,
	paper_id not null,
	foreign key(paper_id) references paper_details(paper_id)
);


