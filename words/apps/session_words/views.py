# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from time import gmtime, strftime


def index(request):
	print "index ago"
	if not "allwords" in request.session:
		request.session['allwords']= []
	if not 'words' in request.session:
		request.session['words']={}
	

	return render(request, "word_random/index.html")


def word(request):
	print "initiate word"
	if request.method == "POST":
		print "its a post"
		newword= {
				'word': request.POST['word'],
				'color': request.POST['color'],
				'size': request.POST['size']
			}
		print newword
		tempallwords = request.session['allwords']
		tempallwords.append(newword)
		request.session['allwords']=tempallwords
		print request.session['allwords']
	return redirect('/')

# Create your views here.
