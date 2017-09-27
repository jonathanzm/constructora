from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TipoProducto(models.Model):
	nombre =models.CharField(max_length= 200)

	def __str__(self):
		return"%s"%(self.nombre)
		


class Producto(models.Model):

	 nombre =models.CharField(max_length= 200)
	 precio =models.CharField(max_length=30)
	 medidas =models.CharField(max_length=30)
	 tipo_producto =models.ForeignKey(TipoProducto)

	 

	 def __str__(self):
		return "%s - %s - %s -%s"% (self.nombre, self.precio ,self.medidas, self.tipo_producto)
