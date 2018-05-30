# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect


def index(request):
	response = "Placeholder to later display all the surveys created"
	return HttpResponse(response)
def new(request):
	reponse = "place holder for all new surveys added"
	return HttpResponse(response)
# Create your views here.
