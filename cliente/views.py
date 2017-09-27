
from django.shortcuts import render,redirect
from django import forms
# Create your views here.
from .forms import ClienteForm
from .models import Cliente

# Create your views here.

def cliente_nuevo(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)   
        if form.is_valid():
        	producto= form.save()       
            	return redirect('cliente:cliente_listar')
    else:
        form = ClienteForm()

	return render(request, 'home/cliente_nuevo_form.html',{'form': form})

