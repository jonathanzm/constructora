from django.conf.urls import url , include
from . import views

urlpatterns = [


	url(r'^nuevo/$', views.producto_nuevo, name='producto_nuevo'),
	url(r'^listar/$', views.producto_listar, name='producto_listar'),
	url(r'^tipo/$', views.producto_tipo_nuevo, name='producto_tipo_nuevo'),
	url(r'^tipo_listar/$', views.producto_tipo_listar, name='producto_tipo_listar'),
	url(r'^tipo_editar/(?P<id_tipo>\d+)$', views.producto_tipo_editar, name='producto_tipo_editar'),
	url(r'^tipo_eliminar/(?P<id_tipo>\d+)$', views.producto_tipo_eliminar, name='producto_tipo_eliminar'),
	url(r'^eliminar/(?P<id_producto>\d+)$', views.producto_eliminar, name='producto_eliminar'),
	url(r'^editar/(?P<id_producto>\d+)$', views.producto_editar, name='producto_editar'),
	
	


	

]