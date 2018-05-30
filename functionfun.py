

def Odd_Even(x):
	for count in range(1,2001):
		# if count%2===0:
		# 	print "Number is", count, "This is an even number"
		if count%2!=0:
			print "Number is", count, "This is an odd number"
		else:
			print "Number is", count, "This is an even number"


def multiple(a, b):
	for check in range(0,len(a)):
		a[check]*=b
	return a

# a = [2,4,5]
# c= multiple(a, 3)
# print c




def layered_multiples(list):
	
	
	newlist=[]
	templist=[]
	for y in range (0,len(list)):
		counter=1
		templist=[]

		while counter <=list[y]:
			templist.append(1)
			counter+=1
		newlist.append(templist)
	print newlist
	return newlist


layered_multiples(multiple([1,2,3],3))
	





 


#   return new_array
# x = layered_multiples(multiply([2,4,5],3))
# print x
# # output
# >>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]


# arr=([2,4,5],3)
# print arr[1]



# y=[]


# y.append(1)

# print y