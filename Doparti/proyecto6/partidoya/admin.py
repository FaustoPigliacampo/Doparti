# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import (Jugador,Cancha,Partido)

# Register your models here.
admin.site.register(Jugador)
admin.site.register(Cancha)
admin.site.register(Partido)