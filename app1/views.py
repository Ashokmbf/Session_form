# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.template import RequestContext
from app1.models import User_Details
from app1.models import Qualification_name
from app1.models import Additional_Qualification
from app1.models import Additional_Skills
from django.contrib.auth.models import User

# Create your views here.

def user_detail_view(request):
	if request.method == 'POST':
		name = request.POST.get('user_name', None)
		request.session['name']=name
		print name
		email = request.POST.get('user_email',None)
		print email
		phone = request.POST.get('user_phone',None)
		print phone
		city = request.POST.get('user_city',None)
		print city
		country = request.POST.get('user_country',None)
		print country
		
	return render(request,'user_details.html')

def qualification_view(request):
	return render(request,'qualification.html')
def preview(request):
	return render(request,'preview.html')			
