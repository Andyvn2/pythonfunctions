from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("dojo_index.html")










app.run(debug=True)