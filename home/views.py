from django.shortcuts import render

# Create your views here.


def mostrar_inicio(request):
	return render(request, 'home/index.html',{})

def mostrar_contactos(request):
	return render(request, 'home/contact.html',{})

def mostrar_quienes(request):
	return render(request, 'home/elements.html',{})

def mostrar_carro(request):
	return render(request, 'producto/shopping-cart.html',{})

def mostrar_maquinaria(request):
	return render(request, 'home/maquinaria.html',{})


def mostrar_herramienta(request):
	return render(request, 'home/herramienta.html',{})


def mostrar_detalle(request):
	return render(request, 'home/detalle_reserva.html',{})

def mostrar_login(request):
	return render(request, 'home/login.html',{})

def mostrar_alquiler(request):
	return render(request, 'aplicacion/index1.html',{})

# administrador