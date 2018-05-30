from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	print session["counter"]
	# session["counter"]=1
	# session["counter"]+=1
	if "counter" in session:
		session["counter"]+=1
	else:
		session["counter"]=1
	return render_template("counter.html", counter=session["counter"])












app.run(debug=True)