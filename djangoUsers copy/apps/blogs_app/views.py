from django.shortcuts import render, HttpResponse, redirect


def index(request):
	response = "Placeholder to later display all the list of blogs"
	return HttpResponse(response)


def news(request):
	response = "Placeholder for a new post"
	return HttpResponse(response)


def create(request):
	return redirect('/')


def show(request, number):
	print "running request"
	response = "Place holder to display blog" +" " ,  number
	return HttpResponse(response)

def edit(request, number):
	print "running request edit"
	response = "Place holder to edit blog" + " ", number
	return HttpResponse(response)
 

def destroy(request, number):
	return redirect("/")