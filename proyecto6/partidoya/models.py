# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models

# Create your models here.

class Jugador (models.Model):
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL)
	telefono = models.IntegerField()
	edad = models.IntegerField()

class Cancha (models.Model):
	nombre = models.CharField(max_length=200)
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL)
	telefono = models.IntegerField()
	direccion = models.CharField(max_length=500)
	imagen = models.ImageField(upload_to='static/img', default='null')
	tipodecancha = models.CharField(max_length=100)
	precios = models.CharField(max_length=200)


class Partido (models.Model):
	jugadores = models.ManyToManyField(Jugador)
	hora = models.IntegerField()
	cancha = models.ForeignKey(Cancha)











