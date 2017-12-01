from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from partidoya.models import Cancha
from django import forms

class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields =[
                'username',
                'first_name',
                'last_name',
                'email',

            ]
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Email',
        }

class CanchaForm(forms.ModelForm):

    class Meta:
        model = Cancha

        fields = [
            'nombre',
            'usuario',
            'telefono',
            'direccion',
            'tipodecancha',
            'precios',
        ]
        labels = {
            'nombre':'Nombre',
            'usuario':'Usuario',
            'telefono':'Telefono',
            'direccion':'Direccion',
            'tipodecancha':'Tipo de cancha',
            'precios':'Precio',
        }
        '''
        widgets = {
            'nombre': forms.askstring(attrs={'class':'form-control'}),
            'usuario': forms.Select(attrs={'class':'form-control'}),
            'telefono': forms.raw_input(attrs={'class':'form-control'}),
            'direccion': forms.askstring(attrs={'class':'form-control'}),
            'tipodecancha': forms.raw_input(attrs={'class':'form-control'}),
            'precios': forms.raw_input(attrs={'class':'form-control'}),
        }
        '''