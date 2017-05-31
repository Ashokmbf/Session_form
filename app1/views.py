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
	request.session['user'] = {}
	if request.method == 'POST':
		
		name = request.POST.get('user_name', None)
		email = request.POST.get('user_email',None)
		phone = request.POST.get('user_phone',None)
		city = request.POST.get('user_city',None)
		country = request.POST.get('user_country',None)
		request.session['user']['name'] = request.POST['name']
		print request.session['user']['name'] 
		request.session['user']['email'] = request.POST['email']
		print request.session['user']['email']
		request.session['user']['phone'] = request.POST['phone']
		print request.session['user']['phone']
		request.session['user']['city'] = request.POST['city']
		print request.session['user']['city']
		request.session['user']['country'] = request.POST['country']
		print 111111111111
		
		return render(request,'qualification.html')
	
		
		
	return render(request,'user_details.html')

def qualification_view(request):
	return render(request,'qualification.html')
def preview(request):
	return render(request,'preview.html')			


