from django.shortcuts import render,redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django import forms
# Create your views here.
from .forms import ProductoForm, TipoProductoForm
from .models import Producto, TipoProducto
from cart.cart import Cart


def producto_nuevo(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)   
        if form.is_valid():
        	producto= form.save()       
        	return redirect('producto:producto_listar')
    else:
        form = ProductoForm()

    return render(request, 'producto/producto_nuevo_form.html', {'form': form})



def producto_listar(request):
	productos=Producto.objects.all()
	context={
			'productos': productos,

	}
	return render(request,'producto/producto_lista_form.html',context)

def producto_eliminar(request, id_producto):
        obj_producto = Producto.objects.get(id=id_producto)
        if request.method=="POST":
                obj_producto.delete()
                return redirect('producto:producto_listar')

        return render(request, 'producto/producto_eliminar_form.html', {'producto':obj_producto})

def producto_editar(request, id_producto):
    producto= Producto.objects.get(id=id_producto)
    if request.method=="POST":
          form = ProductoForm(request.POST, instance=producto) 
          if form.is_valid():
            producto= form.save()       
            return redirect('producto:producto_listar')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'producto/producto_editar_form.html',{'form': form})


# TIPO PRODUCTO

def producto_tipo_nuevo(request):
    if request.method == 'POST':
        form = TipoProductoForm(request.POST)   
        if form.is_valid():
            tipo= form.save()       
            return redirect('producto:producto_listar')
    else:
        form = TipoProductoForm()

    return render(request, 'producto/producto_tipo_form.html',{'form': form})


def producto_tipo_listar(request):
    tipo_producto=TipoProducto.objects.all()
    context={
            'tipo_producto': tipo_producto,

    }
    return render(request,'producto/producto_tipo_lista_form.html',context)

def producto_tipo_eliminar(request, id_tipo):
        obj_tipo = TipoProducto.objects.get(id=id_tipo)
        if request.method=="POST":
                obj_tipo.delete()
                return redirect('producto:producto_listar')

        return render(request, 'producto/producto_tipo_eliminar_form.html', {'producto':obj_tipo})

def producto_tipo_editar(request, id_tipo):
    tipo= TipoProducto.objects.get(id=id_tipo)
    if request.method=="POST":
          form = TipoProductoForm(request.POST, instance=tipo) 
          if form.is_valid():
            tipo= form.save()       
            return redirect('producto:producto_listar')
    else:
        form = TipoProductoForm(instance=tipo)

    return render(request, 'producto/producto_tipo_editar_form.html',{'form': form})


# agregar a carrito
@login_required()
def add_to_cart(request, id_producto, quantity):
    product = Producto.objects.get(id=id_producto)
    cart = Cart(request)
    
    cart.add(product, product.precio_dia, quantity)
    response= HttpResponseRedirect(request.GET.get('next'))
    return response
#@login_required()
def remove_from_cart(request, id_producto):
    product = Producto.objects.get(id=id_producto)
    cart = Cart(request)
    cart.remove(product)
    response= HttpResponseRedirect(request.GET.get('next'))
    return response
#@login_required()
def get_cart(request):
    cart= Cart(request)
    context={
        'cart': cart

    }
    return render(request, 'producto/shopping-cart.html', context)