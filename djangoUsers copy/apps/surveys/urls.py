from django.conf.urls import url
from . import views           # This line is new!


print "i am surveys urls.py"



urlpatterns = [
	url(r'^surveys$', views.index),
	url(r'^surveys/new$', views.new)
	
  ]