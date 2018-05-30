from django.conf.urls import url
from . import views           # This line is new!


print "i am users urls.py"



urlpatterns = [
	url(r'^$', views.index),
	url(r'^/new$', views.new),
	url(r'^/(?P<id>\d+)/edit$', views.edit),
	url(r'^/(?P<id>\d+)$', views.show),
	url(r'^/(?P<id>\d+)/destroy$', views.destroy),
	url(r'^/login$', views.login),
	url(r'^/create$', views.create),
	url(r'^/(?P<id>\d+)/update$', views.update)
  ]