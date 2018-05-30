# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from time import gmtime, strftime


# Create your views here.
def index(request):
	
	# if request.session["counter"] == "":
	# 	request.session['counter']= 1
	# 	temporarycounter =request.session['counter']
	# if request.session["counter"]>0:
	# 	temporarycounter =request.session['counter']
	# 	temporarycounter += 1
	# print "************",temporarycounter
	# random.session["counter"]=temporarycounter
	if "counter" not in request.session:
		request.session['counter'] = 1
	else: 
		request.session['counter']+=1
	print "****************",request.session['counter']
	 
	return render(request, "word_random/index.html")


def random(request):
	# print request.session['counter']
	# print "hello"
	unique_id = get_random_string(length=14)
	print unique_id
	if request.method == "POST":
		request.session["random_word"]=unique_id
		print "helloPOST"
		
		word = unique_id
		return redirect('/', word=word)
	else:
		return redirect('/')

def reset(request):
	request.session.clear()
	return redirect('/')