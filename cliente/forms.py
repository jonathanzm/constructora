from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm, PasswordChangeForm
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext_lazy as _

from cliente.models import Cliente

class ClienteCreationForm(UserCreationForm):
	# def __init__(self, *args, **kargs):
	# 	super(ClienteCreationForm, self).__init__(*args, **kargs)
	# 	del self.fields['username']

	class Meta:
		model = Cliente
		fields = UserCreationForm.Meta.fields + ('email', 'cedula')


class ClienteChangeForm(forms.ModelForm):
	password = ReadOnlyPasswordHashField(label= ("Clave"),
		help_text= ("La clave esta encriptada, asi que no hay forma de ver "
		"la clave de este usuario, pero puede cambiarla usando "
		" <a href=\'../password/\'>este formulario</a>.")
		)

	class Meta:
		model = Cliente
		fields = ('id', 'username','cedula', 'email', 'password', 'is_active',)

	def clean_password(self):
		# Regardless of what the user provides, return the initial value.
		# This is done here, rather than on the field, because the
		# field does not have access to the initial value
		return self.initial["password"]

class ClientePasswordChangeForm(PasswordChangeForm):

    class Meta:
        model = Cliente


class ClienteForm(object):
	class Meta:
		model = Cliente
		fields = UserCreationForm.Meta.fields
		
