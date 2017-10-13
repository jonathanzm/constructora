
from django.conf.urls import url , include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from django.contrib.auth.views import login
urlpatterns = [
    url(r'^', include('home.urls' ,namespace='home')),
    url(r'^admin/', admin.site.urls),




    # para  la app de producto


    url(r'^producto/', include('producto.urls' ,namespace='producto')),

     # para  la app de cliente

    url(r'^cliente/', include('cliente.urls' ,namespace='cliente')),


    #url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),




   

  

    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
