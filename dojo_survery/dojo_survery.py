from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("dojo_index.html")


@app.route('/survey', methods=['POST'])
def process():
	print "got survey info"
	request.form['name']
	name=request.form['name']
	location=request.form['Location']
	language=request.form['Favorite Language']
	description= request.form['description']
	return render_template("survey.html", name=request.form['name'], location=request.form['Location'], language=request.form['Favorite Language'],description= request.form['description'] )








app.run(debug=True)