"""
URL configuration for blogevacovarte project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from articulos import views  # aqui llamamos a las vistas creadas en articulos
from django.conf import settings       #importa el objeto que tiene todo el settingd
from django.conf.urls.static import static      #importa una funcion lalamada static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home,name='home'),       #cuando el usuario este en home se mostrata lo definido en la funcion home que se encuentra en vista
    path('contacto',views.contacto,name='contacto'),   #se pudo asi
    path('nosotros',views.nosotros,name='nosotros'),
    path('servicios',views.servicios,name='servicios'),
    path('base',views.base),
    path('tinymce/',include('tinymce.urls')),
  
    

]
# debug o sea no para subir.Configurara un engineb AVERIGUAR

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

