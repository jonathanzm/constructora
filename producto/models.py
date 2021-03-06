
from django.db import models

# Create your models here.

class TipoProducto(models.Model):
	nombre =models.CharField(max_length= 200)

	def __str__(self):
		return"%s"%(self.nombre)
		


class Producto(models.Model):
	image = models.FileField(null=True, blank=True)
	nombre =models.CharField(max_length= 200)
	precio_dia =models.CharField(max_length= 200)
	#precio_semanal =models.CharField(max_length= 200)
	#precio_mensual =models.CharField(max_length= 200)
	descripcion =models.TextField(max_length=25)
	stock =models.CharField(max_length= 200)
	tipo_producto =models.ForeignKey(TipoProducto)

	 

	def __str__(self):
		return "%s - %s - %s - %s - %s"%(self.nombre, self.precio_dia,self.descripcion, self.stock, self.tipo_producto)
