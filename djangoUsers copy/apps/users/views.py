from django.shortcuts import render, HttpResponse, redirect
from  models import *

def index(request):
	print "Users Page is ready to go"
	# context= {
	# 		"id": User.objects.first().id,
	# 		"full_name": User.objects.all().first_name + User.objects.all().last_name,
	# 		"email_address": User.objects.all().email_address
	# }
	print User.objects.all()
	return render(request,"users/index.html", {"Users": User.objects.all()})
def new(request):
	print "initiate New user page"
	return render(request, "users/new.html")
def create(request):
	if request.method=="POST":
		print "Its a POST"
		first_name    =request.POST["first_name"]
		last_name     = request.POST["last_name"]
		email_address = request.POST["email_address"]
		user = {
			"first_name"   : first_name,
			"last_name"    : last_name,
			"email_address": email_address
		        }
		User.objects.create(first_name=first_name,last_name=last_name, email_address=email_address)
		return redirect('/users/new')
def edit(request,id):
	print " placeholder to edit"," ", id," ", "user"
	return render(request, "users/edit.html", {"User": User.objects.get(id=id)})
def update(request,id):
	if request.method=="POST":
		print "Its an EDIT"
		first_name    =request.POST["first_name"]
		last_name     = request.POST["last_name"]
		email_address = request.POST["email_address"]
		A= User.objects.get(id=id)
		A.first_name = first_name
		A.last_name  = last_name
		A.email_address = email_address
		A.save()
	return redirect("/users")
def login(request):
	response = "Placeholder users to login"
	return HttpResponse(response)
def show(request, id):
	print " placeholder to show", id
	return render(request, "users/user.html", {"User": User.objects.get(id=id)})
def destroy(request,id):
	B= User.objects.get(id=id)
	B.delete()
	return redirect('/users')

