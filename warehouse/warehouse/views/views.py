from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template import Context, loader


# for general and small sized views 

def signupSuccess(request):
	template = loader.get_template('signupsuccess.html')
	return HttpResponse(template.render())

def logoutUser(request):
	logout(request)
	return HttpResponseRedirect('/login/')
