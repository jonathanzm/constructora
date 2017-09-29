
from django.shortcuts import render,redirect
from django import forms
# Create your views here.
from .forms import ClienteCreationForm
from .models import Cliente

# Create your views here.
def authentication(request):
	User = settings.AUTH_USER_MODEL
	error_message=''

	if not request.user.is_authenticated:
		if request.method == 'POST':
			action = request.POST.get('action', None)
			username  = request.POST.get('username', None)
			password = request.POST.get('password', None)

			user = authenticate(username = username, password = password)
			if user is not None:

				login(request, user)

				page_title = 'Index'
				template = 'index.html'

				context = {
					# 'object_list': propuestas,
					'page_title': page_title,
				}
				# return render(request, template, context)
				return redirect('user:index')
			else:
				# mensaje de 'cuenta desactivada'
				error_message='Credenciales invalidas'
				context = {
					'error_message': error_message,
				}

				return render(request, 'login.html', context)

	else:
		return redirect('user:index')
				
	return render(request, 'home/login.html', {})


def cliente_nuevo(request):
	if request.method == 'POST':
		form = ClienteCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('cliente:cliente_listar')
	else:
		form = ClienteCreationForm()
	return render(request, 'home/cliente_nuevo_form.html', {'form': form})




