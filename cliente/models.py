from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Cliente(models.Model):



	nombres =models.CharField(max_length= 200)
	apellidos =models.CharField(max_length= 200)
	cedula =models.CharField(max_length= 200)
	direccion =models.CharField(max_length= 200)
	telefono =models.CharField(max_length=30)
	

	 

	def __str__(self):
		return "%s - %s - %s - %s - %s"%(self.nombres, self.apellidos, self.cedula, self.direccion ,self.telefono)
