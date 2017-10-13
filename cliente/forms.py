from django import forms
from django.contrib.auth.models import User

from .models import Cliente


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')
        labels = {
        	'first_name': 'Nombres',
        	'last_name': 'Apellidos',
        }
        widgets = {
            'password':  forms.PasswordInput(),
        }


class ClienteForm(forms.ModelForm):

	class Meta:
		model= Cliente
		fields = ('cedula', 'direccion', 'telefono')
