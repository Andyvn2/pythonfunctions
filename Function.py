Functions


#####################################################################


def say_hi(name):
  print "Hi, " + name



 Name is a parameter

say_hi('Michael')
say_hi('Anna')
say_hi('Eli') <<<< arguments

def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b
# output:
>>>[10,20,50,80]

#####################################################################


count=0
for count in range (0,1001):
	if count %2 != 0:
		print count


fives = 5
for fives in range (5,1000000):
	if fives % 5 == 0:
		print fives



a = [1, 2, 5, 10, 255, 3]
a.sort()

print a
b = 0

for a in a:
	b+=a
print b


a = [1, 2, 5, 10, 255, 3]
a.sort()

print a
b = 0
count=0
for a in a:
	b+=a
	count+=1
print b/count



#####################################################################



# row1= "1"+" "+"2"+" "+"3"+" "+"4"+" "+"5"+" "+"6"+" "+"7"+" "+"8"+" "+"9"

# row1=[1,2,3,4,5,6,7,8,9,10,11,12]

# # x=1
# # y=row1

# for ind in row1:
# 	print ind*1


print "x", " 1"," 2"," 3"," 4"," 5"," 6"," 7"," 8"," 9"," 10"," 11"," 12"

for i in range(1,13):
	print i, 1*i,2*i,3*i,4*i,5*i,6*i,7*i,8*i,9*i,10*i,11*i,12*i



#####################################################################



a= ['magical unicorns',19,'hello',98.98,'world']


newsum = 0
newstring = ""

if type(a)==int or type(a)==float or type(a)==str:
	for index in a:
		if type(index)==int or type(index)==float:
			newsum+=index
			
		elif type(index)==str:
			newstring+=" "+index
		

	print "Sum:", newsum
	print  "New String:", newstring



newsum2=0
if type(a)==int:
	for index in l:
		newsum2+=index
	print "the list you entered is of integer type"
	print "Sum:", newsum2



newstring2=0
if type(a)==str:
	for index in m:
		newstring2+=index
	print "the list you entered is of string type"
	pring "Sting:", newstring2


#####################################################################


def draw_stars(x):

	for counter in range(0,len(x)):
		print x[counter]*"*"



x = [4, 6, 1, 3, 5, 7, 25]

draw_stars(x)


def draw_stars(x):

	for counter in range(0,len(x)):
		if type(x[counter])==int:
			print x[counter]*"*"
		else:
			y=x[counter]

			y= y.lower()

			
			print x[counter].count("")* y[0]



x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

draw_stars(x)


