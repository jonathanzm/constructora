from django.contrib import admin

# Register your models here.

from .models import Producto, TipoProducto

class AdminProducto(admin.ModelAdmin):
	list_display = ['nombre','precio_dia','precio_semanal','precio_mensual','descripcion','stock','tipo_producto']
	search_fields=['nombre']
	class Meta:
	 	model= Producto
admin.site.register(Producto,AdminProducto)


class AdminTipoProducto(admin.ModelAdmin):
	list_display = ['nombre']
	search_fields=['nombre']
	class Meta:
	 	model= TipoProducto
admin.site.register(TipoProducto,AdminTipoProducto)


