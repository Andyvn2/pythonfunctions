name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def makingdict(list1,list2):
	new_dict = zip(list1, list2)
	new_dict= dict(new_dict)
	print new_dict
	return new_dict

makingdict(name, favorite_animal)