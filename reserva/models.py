from __future__ import unicode_literals

from django.db import models

# Create your models here.


# Create your models here.



class Reserva(models.Model):
	nombre_cliente =models.CharField(max_length= 200)
	fecha =models.CharField(max_length= 200)
	productos=models.CharField(max_length= 200)
	cantidad =models.CharField(max_length= 200)
	abono=models.TextField(max_length=200)
	

	 

	def __str__(self):
		return "%s - %s - %s - %s -%s"%(self.nombre_cliente, self.fecha, self.productos, self.cantidad, self.abono)
