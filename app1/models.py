# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# class User_Details(models.Model):
#     name = models.CharField(max_length = 225, null=True, blank=True) 
#     phone = models.CharField(max_length = 100, null=True, blank=True) 
#     email = models.EmailField(max_length=225)
#     city = models.CharField(max_length = 225, null=True, blank=True)
#     country = models.CharField(max_length = 100, null=True, blank=True)
# class Qualification(models.Model):
    
# class Additional_Qualification(models.Model):
       
# class Additional_Skills(models.Model):
          
# class Languages_known(models.Model):
class User_Details(models.Model):
	user_name=models.CharField(max_length=225, null=True, blank=True)
	user_email=models.CharField(max_length=225, null=True, blank=True)
	user_phone=models.EmailField(max_length=225)
	user_city=models.EmailField(max_length=225)
	user_country=models.EmailField(max_length=225)



class Qualification_name(models.Model):
	qual_list=models.CharField(max_length=225, null=True, blank=True)

class Qualification(models.Model):
	qual_list=models.CharField(max_length=225, null=True, blank=True)
	school_or_college=models.CharField(max_length=225, null=True, blank=True)
	percentage=models.CharField(max_length=225, null=True, blank=True)	
   	 		    
class languages(models.Model):
	language_list=models.CharField(max_length=225, null=True, blank=True)   

class languages_known(models.Model):
	language_list=models.CharField(max_length=225, null=True, blank=True)   

class Additional_Qualification(models.Model):
	language_list=models.CharField(max_length=225, null=True, blank=True)

class Additional_Skills(models.Model):
	skills=models.CharField(max_length=225, null=True, blank=True)
