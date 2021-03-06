from flask import Flask, render_template		# Import Flask to allow us to create our app.

app = Flask(__name__)		 # Global variable __name__ tells Flask whether or not we are running the file
                       		  # directly, or importing it as a module.
                       		   # The "@" symbol designates a "decorator" which attaches the following
                       		    #function to the '/' route. This means that whenever we send a request to
                       		    # localhost:5000/ we will run the following "hello_world" function.
@app.route('/') #You must do this for every route that you want to add to our application. 
def hello_world():
	# return "hello world!"
	return render_template('index.html', name="jay")



app.run(debug=True)