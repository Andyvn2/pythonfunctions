from __future__ import unicode_literals
    
from django.db import models
import re

# Create your models here.
EMAIL_REGEX= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX= re.compile(r'^[a-zA-Z]')




class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if not NAME_REGEX.match(postData['first_name']) or len(postData['first_name']) < 2:
            errors["first_name"] = "First Name should be more than 2 characters"
        if not NAME_REGEX.match(postData['last_name']) or len(postData['last_name']) < 2:
            errors["last_name"] = "Last Name should be more than 2 characters"
        if not EMAIL_REGEX.match(postData['email']) or len(postData['email']) < 2:
            errors["email"] = "Email is Invalid Example: andy@uci.edu"
        if len(postData['new_password']) < 8 :
            errors["new_password"] = "Password is invalid. Must be atleast 8 Characters"
        if not postData["new_password"] == postData["confirm_password"]:
        	errors["confirm_password"] = "Passwords do not match"
        return errors
    def login_validator(self, postData):
        errors = {}
        if postData["login_email"]== "":
            errors["login_email"] = "Email is Empty"
        elif len(User.objects.filter(email=postData["login_email"])) ==0 :
            errors["login_email"]= "Email does not exist"
        else:
            hash1 = User.objects.filter(email=postData['login_email'])[0].password
            if not bcrypt.checkpw(postData["login_password"].encode(), hash1.encode()):
                print "pw is wrong"
                errors["login_password"]= "Invalid"
        return errors
    



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name =  models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password= models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=UserManager()
