from django.shortcuts import render,redirect
from django import forms
# Create your views here.
from .forms import ClienteCreationForm
from .models import Cliente

<<<<<<< HEAD
=======
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
>>>>>>> df24d45e659265e23318ffa9b13316302bbd27af


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






def cliente_listar(request):
	clientes=Cliente.objects.all()
	context={
			'clientes': clientes,

	}
	return render(request,'home/cliente_listar_form.html',context)

def cliente_eliminar(request, id_cliente):
        obj_cliente = Cliente.objects.get(id=id_cliente)
        if request.method=="POST":
                obj_cliente.delete()
                return redirect('cliente:cliente_listar')

        return render(request, 'home/cliente_eliminar_form.html', {'cliente':obj_cliente})

def cliente_editar(request, id_cliente):
    cliente= Cliente.objects.get(id=id_cliente)
    if request.method=="POST":
          form = ClienteForm(request.POST, instance=cliente) 
          if form.is_valid():
            cliente= form.save()       
            return redirect('cliente:cliente_listar')
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'home/cliente_editar_form.html',{'form': form})