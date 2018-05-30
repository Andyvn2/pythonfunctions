from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
  return render_template("ninjahtml.html")


@app.route('/ninjas')
def ninjas():

    return render_template("ninjas.html")


@app.route('/ninjas/<color>')
def turtle(color):
    print color
    return render_template("ninja2.html", color=color)

# @app.route('/users/<red>')
# def show_user_profile(color):
#     print username
#     return render_template("ninja2.html", color=color)

# @app.route('/users/<purple>')
# def show_user_profile(color):
#     print username
#     return render_template("ninja2.html", color=color )

# @app.route('/users/<orange>')
# def show_user_profile(username):
#     print username
#     return render_template("ninja2.html")



app.run(debug=True) # run our server
