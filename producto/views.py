from django.shortcuts import render,redirect
from django import forms
# Create your views here.
from .forms import ProductoForm, TipoProductoForm
from .models import Producto, TipoProducto



def producto_nuevo(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)   
        if form.is_valid():
        	producto= form.save()       
        	return redirect('producto:producto_listar')
    else:
        form = ProductoForm()

    return render(request, 'home/producto_nuevo_form.html', {'form': form})



def producto_listar(request):
	productos=Producto.objects.all()
	context={
			'productos': productos,

	}
	return render(request,'home/producto_lista_form.html',context)

def producto_eliminar(request, id_producto):
        obj_producto = Producto.objects.get(id=id_producto)
        if request.method=="POST":
                obj_producto.delete()
                return redirect('producto:producto_listar')

        return render(request, 'home/producto_eliminar_form.html', {'producto':obj_producto})

def producto_editar(request, id_producto):
    producto= Producto.objects.get(id=id_producto)
    if request.method=="POST":
          form = ProductoForm(request.POST, instance=producto) 
          if form.is_valid():
            producto= form.save()       
            return redirect('producto:producto_listar')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'home/producto_editar_form.html',{'form': form})


# TIPO PRODUCTO

def producto_tipo_nuevo(request):
    if request.method == 'POST':
        form = TipoProductoForm(request.POST)   
        if form.is_valid():
            tipo= form.save()       
            return redirect('producto:producto_listar')
    else:
        form = TipoProductoForm()

    return render(request, 'home/producto_tipo_form.html',{'form': form})


def producto_tipo_listar(request):
    tipo_producto=TipoProducto.objects.all()
    context={
            'tipo_producto': tipo_producto,

    }
    return render(request,'home/producto_tipo_lista_form.html',context)

def producto_tipo_eliminar(request, id_tipo):
        obj_tipo = TipoProducto.objects.get(id=id_tipo)
        if request.method=="POST":
                obj_tipo.delete()
                return redirect('producto:producto_listar')

        return render(request, 'home/producto_tipo_eliminar_form.html', {'producto':obj_tipo})

def producto_tipo_editar(request, id_tipo):
    tipo= TipoProducto.objects.get(id=id_tipo)
    if request.method=="POST":
          form = TipoProductoForm(request.POST, instance=tipo) 
          if form.is_valid():
            tipo= form.save()       
            return redirect('producto:producto_listar')
    else:
        form = TipoProductoForm(instance=tipo)

    return render(request, 'home/producto_tipo_editar_form.html',{'form': form})

