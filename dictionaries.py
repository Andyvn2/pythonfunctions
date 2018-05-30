def makingandreading():
	context = {
		'My': [
	 	{'id': "name is Andy"},
		{'id': "age is 24"},
  		{'id': "country of birth is the United States"},
   		{'id': "Favorite lanaguage is Python"}
 		 ]
 	}

 	for key, data in context.items():
     		for value in data:
          		print "My", value["id"]

makingandreading()