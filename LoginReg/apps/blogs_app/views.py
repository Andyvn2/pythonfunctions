from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from models import *

def index(request):
	response = "Placeholder to later display login and registration"
	
	return render(request, "blogs_app/index.html")

def create(request):
	print "create new account"
	if request.method == "POST":
		errors = User.objects.basic_validator(request.POST)
		if len(errors):
			for tag, error in errors.iteritems():
				messages.error(request, error, extra_tags=tag)
		else:
				
				first_name= request.POST["first_name"]
				last_name = request.POST["last_name"]
				email     = request.POST["email"]
				password  = bcrypt.hashpw(request.POST["new_password"].encode(), bcrypt.gensalt())
				User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
				print "REGISTER COMPLETED"
	return redirect('/')

def login(request):
	if request.method == "POST":
		errors = User.objects.loginValidator(request.POST)
		if len(errors):
			for tag, error in errors.iteritems():
				messages.error(request, error, extra_tags=tag)
		else:
			return redirect('/success')
		# login = request.POST["login_email"]
		# print "Found a match"
		# hash1 = User.objects.filter(email=login)[0].password
		# if bcrypt.checkpw(request.POST["login_password"].encode(), hash1.encode()):
		# 	return redirect('/success')
	return redirect('/')

def success(request):
	return render(request, "blogs_app/success.html")


# def news(request):
# 	response = "Placeholder for a new post"
# 	return HttpResponse(response)


# def create(request):
# 	print "create initiate"
# 	if request.method == "POST":
# 		print "*"*50
# 		print request.POST['name']
# 		print request.POST['desc']
# 		request.session['name']= request.POST['name']
# 		print '*'*50
# 		print request.session['name']
# 		return redirect('/')
# 	else:
# 		return redirect('/')



	# 	print "*"*50
	# 	print request.POST
 #        print request.POST['name']
 #        print request.POST['desc']
 #        request.session['name'] = "test"  # more on session below
	# 	print "*"*50
	# 	return redirect("/")
	# else:
	# 	return redirect("/")


# def show(request, number):
# 	print "running request"
# 	response = "Place holder to display blog" +" " ,  number
# 	return HttpResponse(response)

# def edit(request, number):
# 	print "running request edit"
# 	response = "Place holder to edit blog" + " ", number
# 	return HttpResponse(response)
 

# def destroy(request, number):
# 	return redirect("/")