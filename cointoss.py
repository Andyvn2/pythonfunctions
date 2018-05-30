import random

def cointoss(x):
 	
	for toss in range(0,5001):
		head=0
 		tails=0
		random_num = random.randint(0,1)
		if random_num == 1:
			head+=1
			print "Attempt #",toss,": Throwing a coin... Its a head! .... Got", head,"(s) so far and", tails,"tail(s) so far"
		if random_num == 0:
			tails+=1
			print "Attempt #",toss,": Throwing a coin... Its a tails! .... Got", head,"(s) so far and", tails,"tail(s) so far"
		


cointoss(0)