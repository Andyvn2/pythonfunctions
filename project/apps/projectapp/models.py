from __future__ import unicode_literals
import bcrypt
from django.db import models
import re

# Create your models here.
EMAIL_REGEX= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX= re.compile(r'^[a-zA-Z]')



class User(models.Model):
	name 	=models.CharField(max_length=255)
	username=models.CharField(max_length=255)
	password=models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add= True)
	updated_at =DateTimeField(auto_now= True)
	