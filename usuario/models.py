from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Usuario(models.Model):
	username=models.CharField(max_length= 200)
	password=models.CharField(max_length= 200)
	

	 

	def __str__(self):
		return "%s - %s - %s - %s -%s"%(self.nombre_cliente, self.fecha)
