from django.conf.urls import url , include
from . import views

urlpatterns = [


	url(r'^nuevo/$', views.cliente_nuevo, name='cliente_nuevo'),
	
	


	

]