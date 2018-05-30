import random

def scoresandgrades(x):

	

	x=10
	y=0
	while y<10:
		random_num = random.randint(60,100)
		if random_num<=100 and random_num>90:
			print "Score:", random_num,";", "Your grade is: A",
		if random_num<=90 and random_num>79:
			print "Score:", random_num,";", "Your grade is: B",
		if random_num<=79 and random_num>69:
			print "Score:", random_num,";", "Your grade is: C",
		if random_num<=69 and random_num>60:
			print "Score:", random_num,";", "Your grade is: D",
		y= y+1 
	print "end of the program. Bye!"



scoresandgrades(1)