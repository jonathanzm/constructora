from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Factura(models.Model):
	nombre=models.CharField(max_length= 200)
	apellidos =models.CharField(max_length= 200)
	cedula =models.CharField(max_length= 200)
	direccion =models.CharField(max_length= 200)
	telefono=models.CharField(max_length=200)
	cantidad=models.CharField(max_length=200)
	descuento=models.CharField(max_length=200)
	iva=models.CharField(max_length=200)
	total=models.CharField(max_length=200)
	


	def __str__(self):
		return " %s - %s - %s - %s - %s - %s - %s - %s -%s"%(self.nombre, self.apellidos, self.cedula, self.direccion, self.telefono, self.cantidad, self.descuento, self.iva, self.total)
