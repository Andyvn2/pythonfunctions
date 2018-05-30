ROUTING

# the server is listening for a POST request to:
# localhost:5000/users
# we define the route below such that the route matches the action of our form - '/users'
# similarly we need to allow specific methods - 'POST' in this case
@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"
    # recall the name attributes we added to our form inputs
    # to access the data that the user input into the fields we use request.form['name_of_input']
    name = request.form['name']
    email = request.form['email']
    return redirect('/') # redirects back to the '/' route



    <!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='CSS/my_style_sheet.css') }}">
	<script type="text/javascript" src="{{ url_for('static', filename='my_script.js') }}"></script>
	<title>My first template</title>
</head>
<body>
<h1>My first flask template with embedded python</h1>
<p>phrase {{phrase}}</p>
<p>times: {{ times}}</p>
<p>phrase {{phrase}}</p>
<p>times: {{ times}}</p>
<p>phrase {{phrase}}</p>
<p>times: {{ times}}</p>
<p>phrase {{phrase}}</p>
<p>times: {{ times}}</p>



{% for x in range(0,times+2): %}
     <p>{{ phrase }}</p>     
      {% endfor %}



{% if phrase == "hello" %}
 <p>The phrase says hello</p>
      {% endif %}






<!DOCTYPE html>
<html>
<head>
	<title>DisplayPage</title>
</head>
<body>
<h1>Details on Survey</h1>
<p>{{ name }}</p>
<p>{{ location }}</p>
<p>{{ language }}</p>
<p>{{ description }}</p>

</body>
</html>



>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
					ROUTING EXAMPLE SURVEY

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



<html>
    <head>
       <title>Form Test Index</title>
    </head>
    <body>
      <h1>Index Page</h1>
      <h3>Create a User</h3>
      <!-- read on to learn about form actions, we'll talk about the method in a later section -->
      <form action='/survey' method='post'>
          Name: <input type='text' name='name'>
          Dojo Location: <select name="Location"><option value="Silicon Valley">Silicon Valley</option></select>
          Favorite Language: <select name="Favorite Language"><option value="Javascript">Javascript</option></select>
          <p>A short description about yourself:</p>
          <p><textarea name="description"></textarea></p>
          <input type='submit' value='submit'>
      </form>
    </body>
</html>



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




>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
					ROUTING EXAMPLE SURVEY END

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>





>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
					Sessions, hidden

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
  return render_template("index.html")


@app.route('/user', methods=['POST'])
def create_user():
   session['name'] = request.form['name']
   session['email'] = request.form['email']

   return redirect('/show')

@app.route('/show')
def show_user():
  return render_template('user.html', name=session['name'], email=session['email'])
app.run(debug=True)



IDEX HTML

<html>
    <head>
       <title>Form Test Index</title>
    </head>
    <body>
      <h1>Index Page</h1>
      <h3>Create a User</h3>
      <!-- read on to learn about form actions, we'll talk about the method in a later section -->
      <form action='/user' method='post'>
          Name: <input type='text' name='name'>
          Email: <input type='text' name='email'>
          <input type='submit' value='create user'>
      </form>
    </body>
</html>


USER HTML
<html>
  <head>
    <title>Form Test Show</title>
  </head>
  <body>
    <h1>User:</h1>
    <h3>{{name}}</h3>
    <h3>{{email}}</h3>
  </body>
</html>


Session is a way to store information unique to a particular client
Session uses cookies to store some or all of the required information
When you want to access and modify data over multiple redirects use session
You can use session in both your server.py file as well as your templates
Even though you have access to the session, you should not abuse the amount of information you store in it. Store only what you need in the session. Once we incorporate a database you should be limiting what you store in sessions to the most minimal amount of data possible.



<form method="post" action="/process">
    <input type="hidden" name="action" value="register">
    <input type="text" name="first_name">
    <input type="text" name="last_name">
    <input type="text" name="email">
    <input type="password" name="password">
    <input type="submit" value="Register">
</form>
<form method="post" action="/process">
    <input type="hidden" name="action" value="login">
    <input type="text" name="email">
    <input type="password" name="password">
    <input type="submit" value="Login">
</form>




if request.form['action'] == 'register':
  //do registration process
elif request.form['action'] == 'login':
  //do login process

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
					Sessions

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


