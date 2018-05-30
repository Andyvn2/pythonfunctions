# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

from time import gmtime, strftime


def index(request):
	print "Index good to go!"
	return render(request, "survey_form/index.html")

def survey(request):
	if request.method == "POST":
		request.session['name']=request.POST['name']			#THIS WILL SAVE NAME, LANGUAGE, COMMENT, AND LOCATION
		request.session['favorite_language']=request.POST['favorite_language']
		request.session['location']=request.POST['location']
		request.session['comment']=request.POST['comment']
		print request.POST['favorite_language']
		print request.POST['location']
		print request.session['name']
		print request.POST['comment']
		name=request.session['name']
		language=request.session['favorite_language']
		location=request.session['location']
		comment=request.session['comment']
		print "survey submitted"
	return redirect('/results')

def results(request):
	
	name=request.session['name']
	language=request.session['favorite_language']
	location=request.session['location']
	comment=request.session['comment']
	print "results ready to go"
	return render(request, "survey_form/results.html")
# Create your views here.
