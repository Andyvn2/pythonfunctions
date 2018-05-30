from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector


app = Flask(__name__)
mysql = MySQLConnector(app,'mydb')



app.secret_key = "unicorns"


import re
EMAIL_REGEX= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def index():
	# query = mysql.query_db("SELECT * FROM emails")
	query = "SELECT * FROM emails"
	print query
	email= mysql.query_db(query)
	print email
	return render_template("index3.html", email=email)




@app.route('/email', methods=["POST"])
def create():
	# email=request.form['email']
	# user_query="SELECT * FROM email where emails.email = :email LIMIT 1"
	# # query = mysql.query_db("SELECT * FROM emails")
	# # data = 
	# # print request.form['email']
	if len(request.form['email'])<1:
		flash ("Please enter a password")
	if not EMAIL_REGEX.match(request.form['email']):
		flash("Email is invalid")
	elif EMAIL_REGEX.match(request.form['email']):
		print "valid email address"
		query="INSERT INTO emails (email, created_at) VALUES(:email, now())"	
		data = {
			'email':request.form['email']
			}
		
	# elif len(request.form['email'])>1:
	# 	for x in range(0, len(query)):
	mysql.query_db(query, data)
	return redirect('/success')

@app.route('/success')
def success():
	query= "SELECT * FROM emails"
	email= mysql.query_db(query)
	return render_template("success.html", email=email)






app.run(debug=True)