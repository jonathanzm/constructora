from django.shortcuts import render,redirect
from django import forms
# Create your views here.
from .forms import ClienteForm
from .models import Cliente



def cliente_nuevo(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)   
        if form.is_valid():
        	producto= form.save()       
            	return redirect('cliente:cliente_listar')
    else:
        form = ClienteForm()

	return render(request, 'home/cliente_nuevo_form.html',{'form': form})



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