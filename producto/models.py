from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TipoProducto(models.Model):
	nombre =models.CharField(max_length= 200)

	def __str__(self):
		return"%s"%(self.nombre)
		


class Producto(models.Model):

<<<<<<< HEAD


	nombre =models.CharField(max_length= 200)
	precio_dia =models.CharField(max_length= 200)
	precio_semanal =models.CharField(max_length= 200)
	precio_mensual =models.CharField(max_length= 200)
	descripcion =models.TextField(max_length=200)
	stock =models.CharField(max_length= 200)
	tipo_producto =models.ForeignKey(TipoProducto)

	 

	def __str__(self):
		return "%s - %s - %s - %s - %s - %s -%s"%(self.nombre, self.precio_dia, self.precio_semanal, self.precio_mensual ,self.descripcion, self.stock, self.tipo_producto)
=======
	nombre =models.CharField(max_length= 200)
	precio =models.CharField(max_length=30)
	medidas =models.CharField(max_length=30)
	tipo_producto =models.ForeignKey(TipoProducto)

	def __str__(self):
		return "%s - %s - %s -%s" % (self.nombre, self.precio ,self.medidas, self.tipo_producto)
>>>>>>> df24d45e659265e23318ffa9b13316302bbd27af
