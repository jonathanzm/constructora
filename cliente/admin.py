from django.contrib import admin

from .models import Cliente

# Register your models here.


class AdminCliente(admin.ModelAdmin):
	list_display = ['cedula_identidad','telefono']
	search_fields=['cedula_identidad']
	class Meta:
	 	model= Cliente
admin.site.register(Cliente,AdminCliente)


