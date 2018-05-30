from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'




@app.route('/')
def index():
	import random
	
	if "guessnumber" not in session:
		session["guessnumber"] = random.randrange(0, 101)
	
	print "hi"
	# print guess_number
	print session["guessnumber"]
	print session["guess_number"]
	
	# if int(session["guess_number"])>session["guessnumber"]:
	# 	session["guess"]= "Guess is too High"
	# 	print session["guess"]
	

	# if int(session["guess_number"])==session["guessnumber"]:
	# 	session["guess"]= "Guess is RIGHT"		
	# 	# 
	# 	print session["guess"]
	# 	return redirect ("/reset")
	

	# if int(session["guess_number"])<session["guessnumber"]:
	# 	session["guess"]= "Guess is too Low"
	# 	print session["guess"]

	# if "guess_number" not in session:
	# 	session["guess_number"]="1"

	# if "guessnumber" not in session:
	# 	session["guessnumber"]= "1"






	return render_template("numbergame.html", guessnumber=session["guessnumber"], guess_number=session["guess_number"],guess=session["guess"])
   	# return redirect('/show')



@app.route('/reset')
def reset():	
	import random
	session["guessnumber"]=random.randrange(0,100)
	guessnumber=session["guessnumber"]

	return redirect('/')



@app.route('/guess', methods=['POST'])
def showguess():
   	session["guess_number"] = request.form['Guess']
   	print session["guess_number"]
   	print session["guessnumber"]
  	# print guess_number
  	print "Guess Received"
 	# if session["guess_number"]>session["guessnumber"]:
		# session["guess"]= 1
		# print "guess is too high"

	
	if int(session["guess_number"])>session["guessnumber"]:
		session["guess"]= "Guess is too High"
		print session["guess"]
	

	if int(session["guess_number"])==session["guessnumber"]:
		session["guess"]= "Guess is RIGHT"		
		# 
		print session["guess"]
		return redirect ("/reset")
	

	if int(session["guess_number"])<session["guessnumber"]:
		session["guess"]= "Guess is too Low"
		print session["guess"]

	if "guess_number" not in session:
		session["guess_number"]="1"

	if "guessnumber" not in session:
		session["guessnumber"]= "1"
	
  	return redirect('/')





# @app.route('/show')
# def processguess():
# 	# guess_number=request.form["Guess"]
# 	print "got guess"
# 	print session["guess_number"]
#   	return render_template('numbergame.html', number=session["guessnumber"])













app.run(debug=True)