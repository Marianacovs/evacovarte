# from django.contrib import admin
from django.urls import  path
from articulos import views  # aqui llamamos a las vistas creadas en articulos
from django.conf import settings       #importa el objeto que tiene todo el setting
from django.conf.urls.static import static      #importa una funcion lalamada static




urlpatterns = [
    # path('admin/', admin.site.urls),
    path('home',views.home,name='home'),    #cuando el usuario este en home se mostrata lo definido en la funcion home que se encuentra en vista
    path('contacto',views.contacto,name='contacto'),   #se pudo asi
    path('nosotros',views.nosotros,name='nosotros'),
    path('servicios',views.servicios,name='servicios'),
    path('base',views.base),
    # path('tinymce/',include('tinymce.urls')),
    

]
# debug o sea no para subir.Configurara un engineb AVERIGUAR

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

