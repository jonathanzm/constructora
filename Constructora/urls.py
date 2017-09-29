
from django.conf.urls import url , include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('home.urls' ,namespace='home')),
    url(r'^admin/', admin.site.urls),




    # para  la app de producto


    url(r'^producto/', include('producto.urls' ,namespace='producto')),
     # para  la app de cliente

    url(r'^cliente/', include('cliente.urls' ,namespace='cliente')),

  

    
]
