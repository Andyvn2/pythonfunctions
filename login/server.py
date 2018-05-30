from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
import md5


app = Flask(__name__)
mysql= MySQLConnector(app,'mydb')

app.secret_key = "unicorns"


import re
EMAIL_REGEX= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX= re.compile(r'^[a-zA-Z]')


@app.route('/')
def index():
	print "page ready to go"
	return render_template("login.html")


@app.route('/success')
def success():
	return render_template("success.html")

@app.route('/login', methods=['POST'])
def login():
	print "BEGINNING LOGIIIINNSUUUU"
	email= request.form["email"]
	login_password = request.form["password"]
	print email
	# hashed_password = md5.new(login_password).hexdigest()
	login_query = "SELECT * FROM login WHERE login.email = :email LIMIT 1"
	login_data  = {
					"email": email,
					"password": login_password
					}
	login = mysql.query_db(login_query, login_data)
	print login_data
	if len(login) != 0:
		hashed_password = md5.new(login_password).hexdigest()
		print hashed_password
		if login[0]['password'] == hashed_password:
			flash ("LOGIN IS SUCCESSFURRRRU")
			return redirect("/success")
		else:
			print "PASSWORD IS INCORRECT"
			flash ("PASSWORD IS WRONGG")
			# return redirect("/")
	else:
		print "EMAIL DOES NOT EXIST"
	# 	return redirect("/")
	return redirect("/")


@app.route('/register', methods=["POST"])
def create():
	print "start login"
	if not EMAIL_REGEX.match(request.form['new_email']) or len(request.form['new_email'])<2:
		flash ("Please Enter Valid Email")
		return redirect('/')
	if not NAME_REGEX.match(request.form['first_name']) or len(request.form['first_name'])<2:
		flash ("Please Enter Valid First Name")
		return redirect('/')
	if not NAME_REGEX.match(request.form['last_name']) or len(request.form['last_name'])<2:
		flash ("Please Enter Valid Last Name")
		return redirect('/')
	if not len(request.form['new_password'])>7:
		flash ("You need to enter a password longer than 8 Characters")
		return redirect('/')
	if not request.form['new_password']==request.form['confirm_password']:
		flash ("You need to have matching passwords")
		return redirect('/')
	elif EMAIL_REGEX.match(request.form['new_email']):
		print "YOU'VE SUCCESSFULLY REGISTERED"
		print "Everything is Valid, ENTERING THE DATA BASSEEEEEE"
		
		password = request.form["new_password"]
		hashed_password = md5.new(password).hexdigest()
		print hashed_password
		query="INSERT INTO login (first_name, last_name, email, password, created_at, updated_at) VALUES(:first_name, :last_name, :email, :new_password, now(), now())"	
		data = {
			'first_name':request.form['first_name'],
			'last_name':request.form['last_name'],
			'email':request.form['new_email'],
			'new_password': hashed_password
				}
	mysql.query_db(query, data)
	print "information entered MASTER"
	return redirect('/')








app.run(debug=True)