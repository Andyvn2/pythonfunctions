from django.conf.urls import url, include
from . import views
print "URLs ready to go"

urlpatterns = [
	url(r'^$', views.index),
	url(r'^survey$', views.survey),
	url(r'^results$', views.results)
]