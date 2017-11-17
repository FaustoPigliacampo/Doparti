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
from django.contrib.auth.models import AnonymousUser 
from django.contrib import messages 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from django.db.models import Q 
from django.http import HttpResponse
from .models import Cancha
from datetime import datetime, timedelta 

# Create your views here.

def index(request):
    return render(request,'main.html')

def login(request):
	return render(request,'login.html')

def inicio(request):
	return render(request,'inicio.html')

def canchas_all(request):
    try:
        canchas = Cancha.objects.all().order_by('-nombre')
    except:
        canchas = None
    return render(request,
                    'inicio.html',
                    {'canchas_all':canchas})

def vista_cancha(request):
    nombre1 = request.GET['nombre']
    direccion1 = request.GET['direccion']
    if request.method == 'GET':
        return render(request,
                    'inicio.html',
                    {'canchas_all':canchas})

                    

