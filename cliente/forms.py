from django.forms import ModelForm
from .models import Cliente



class ClienteForm(ModelForm):

	class Meta:
		model= Cliente
		fields = [

            'username',
            'password',
            'nombre',
            'apellidos',
            'cedula',
            'direccion',
            'telefono',
        ]
