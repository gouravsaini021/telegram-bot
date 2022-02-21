from dataclasses import dataclass
@dataclass
class question_set:
	question_nu:int
	question:str
	answer:int
	explanation:str
	paper_id:int

def math_paper():
	return [question_set(1,"""How many prime number in 1 to 10 
		a). 1	b). 2
		c). 4	c). 3""",3,"The prime no between 1 to 10 id 2,3,5,7 which are four in count",1),
	question_set(2,"""(a+b)^2=?
		a). a^2+b^2	 b). a^2+b^2+ab
		c). a^2+b^2+2ab	d). a+b""",3,"(a+b)(a+b)=a^2+b^2+2ab",1),
	question_set(3,"""What is the area of square 
	 1). side+side \t2). side-side 
	 3). side*side \t 4). side/side""",3,"The area of square is side*side",1),
	question_set(4,"""What is the area of rectangle 
	 1). length+breadth  \t 2). length*breadth 
	  3). length-breadth \t 4). length//breadth""",2,"The area of rectangle is length*breadth",1)]



def gk_paper():
	return [	question_set(1,"Who invented Computer? \n 1.charles babbage \t 2. Albert Einstein \n 3.Newton \t 4.Rahul Gandhi ",1,"Charles Babbage is Father of Computer",2),
		question_set(2,"1024 Kilobytes is equal to? \n 1). 1 GB \t2). 1 MB \n 3). 1 TB \t 4). 1 BB",2,"1024 Kilobytes(KB) =1 Mega Bytes(MB)",2),
		question_set(3,"How many players are there in a cricket team? \n 1). 12 \t2). 15 \n 3). 11 \t 4). 22",3,"cricket has 11 players",2),
		question_set(4," Who was the inventor of the light bulb? \n 1. Thomas Edison \t 2.Albert Einstein \n 3. Andrew ng \t 4. Arwind kejriwal",1,"Thomas Edison invented bulb",2)

	]
