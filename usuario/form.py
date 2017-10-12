from django.contrib.auth.models import User


class UserForm(forms.ModelForm):

	password = forms.CharField(widget= forms.PasswordInput)

	class Meta:
		model = User
		fields= ['username', 'email', 'password', 'first_name', 'last_name']


class UsuarioForm (forms.ModelForm):
	password = forms.CharField(widget= forms.PasswordInput)
	class Meta:
		model= Perfil
		fields= [
		'username', 
		'email',
		 'password', 
		 'first_name', 
		 'last_name'
		 ,]

class RegisterForm(forms.Form):
	username= forms.CharField(label = "Nombre de usuario", widget=forms.TextInput())
	email = forms.CharField(label=	"Correo electronico", widget= forms.TextInput())
	password_one= forms.CharField(label= "Password", widget= forms.PasswordInput(render_value= False))
	password_two= forms.CharField(label= " Confirmar Passworrd", widget= forms.PasswordInput(render_value= False))