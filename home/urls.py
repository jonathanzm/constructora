from django.conf.urls import url , include
from . import views



urlpatterns = [
	url(r'^$', views.mostrar_inicio),
	url(r'^contactos/$', views.mostrar_contactos, name='mostrar_contactos'),
	url(r'^shopping-cart/$', views.mostrar_carro, name='mostrar_carro'),
	url(r'^quienes_somos/$', views.mostrar_quienes, name='mostrar_quienes'),
	url(r'^maquinaria/$', views.mostrar_maquinaria, name='mostrar_maquinaria'),
	url(r'^herramientas/$', views.mostrar_herramienta, name='mostrar_herramienta'),
	url(r'^detalle/$', views.mostrar_detalle, name='mostrar_detalle'),
	url(r'^login/$', views.mostrar_login , name='mostrar_login'),

	# admin

	#url(r'^administrador/$', views.mostrar_admin, name='mostrar_admin'),





	#url(r'^register/$', views.UserFormView.as_view(), name='register'),
	#url(r'^new_user/$', views.usuario),
	
	# usuarios
		
	#url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	#url(r'^admin/',views.add_user),

]

