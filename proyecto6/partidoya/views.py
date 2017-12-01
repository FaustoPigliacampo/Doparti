# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from django.core.urlresolvers import reverse 
from django.shortcuts import render_to_response, render, redirect 
from django.template import RequestContext 
from django.conf import settings 
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse 
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.models import AnonymousUser, User
from django.contrib import messages 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from django.db.models import Q 
from django.http import HttpResponse
from .models import Cancha
from datetime import datetime, timedelta 
from django.template.context_processors import csrf
#from .models import MyRegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django import forms as form
from partidoya.forms import RegistroForm, CanchaForm


# Create your views here.

def main(request):
    return render(request,'main.html')

def login(request):
	return render(request,'login.html')

def inicio(request):
	try:
		canchas = Cancha.objects.all().order_by('-nombre')
   	except:
		canchas = None
	return render(request,
                    'inicio.html',
                    {'canchas_all':canchas})	

def register(request):
    form = RegistroForm(data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
    	form.save()
    	return HttpResponseRedirect(reverse('inicio'))
    return render(request, 'registration_form.html', {'form': form})


def crear_cancha(request):
	if request.method == 'POST':
		form = CanchaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('inicio')
	else:
		form = CanchaForm()

	return render(request,'crear_cancha.html',{'form':form})



