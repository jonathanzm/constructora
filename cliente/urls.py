from django.conf.urls import url , include
from . import views

urlpatterns = [


	url(r'^nuevo/$', views.cliente_nuevo, name='cliente_nuevo'),
	url(r'^listar/$', views.cliente_listar, name='cliente_listar'),
	url(r'^eliminar/(?P<id_cliente>\d+)$', views.cliente_eliminar, name='cliente_eliminar'),
	url(r'^editar/(?P<id_cliente>\d+)$', views.cliente_editar, name='cliente_editar'),

]