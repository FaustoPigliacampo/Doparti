# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Partido(models.Model):
    fecha = models.DateField()
    jugadores = models.IntegerField()
    cancha = models.CharField(max_length = 30)