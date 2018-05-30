from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector


app = Flask(__name__)
mysql = MySQLConnector(app,'mydb')




@app.route('/')
def index():
	friend = mysql.query_db("SELECT * FROM friend")
	print friend
	
	return render_template('index2.html', all_friends=friend)

@app.route('/friends', methods=['POST'])
def create():

	print request.form['name']
	print request.form['age']

	query = "INSERT INTO friend (name, age, created_at, updated_at) VALUES(:name, :age, NOW(), NOW())"
	
	data = {
			'name':request.form['name'],
			'age': request.form['age'],
			}
	print "hello"
	mysql.query_db(query, data)
	return redirect('/')


app.run(debug=True)



