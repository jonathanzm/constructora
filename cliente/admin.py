from django.contrib import admin

# Register your models here.

from .models import Cliente

class AdminCliente(admin.ModelAdmin):
	list_display = ['nombres','apellidos','cedula','direccion','telefono']
	search_fields=['nombre']
	class Meta:
	 	model= Cliente
admin.site.register(Cliente,AdminCliente)
