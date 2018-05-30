# def names():
# 	users= {
# 		'students' : [
# 	     {'first_name':  'Michael', 'last_name' : 'Jordan'},
# 	     {'first_name' : 'John', 'last_name' : 'Rosales'},
# 	     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
# 	     {'first_name' : 'KB', 'last_name' : 'Tonel'}
# 	],
# 		'Instructors' : [
#     	{'first_name' : 'Michael', 'last_name' : 'Choi'},
#      	{'first_name' : 'Martin', 'last_name' : 'Puryear'}
#      ]
# 	}	

# 	for key, data in users['students']():
# 		for value in data:
# 			print "Students"
# 			print value["first_name"], value["last_name"] 

# names()


# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# def names(x):
# 	for i in range(0,len(x)):
# 		print x[i].get('first_name',""), x[i].get('last_name',"")

# names(students)


users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def names(x):
	count=0
	counts=0
	# for key, values in users['Students']:
	print "STUDENTS"
	for values in users['Students']:
		
		count+=1
		print  str(count), values["first_name"], values['last_name'], + len(values["first_name"]+values["last_name"])
		

	print "INSTRUCTORS"
	for values in users['Instructors']:
		counts +=1
		print counts, values["first_name"], values['last_name'], + len(values["first_name"]+values["last_name"])
	# 	for students in range(1,len('Students')):
	# 		print .get('first_name', "")

names(users)