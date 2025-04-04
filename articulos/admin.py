from django.contrib import admin
from articulos.models import Contacto, Entradas,EntradaDos,Servicios   # importar para que se vea en el administrador

from tinymce.widgets import TinyMCE      # importar el editor de texto
from django.db import models             # importar modelos 

# se crea una nueva clase que hereda del admin.ModelAdmin
class ProyectoAdmin(admin.ModelAdmin):    
    formfield_overrides={
        models.TextField:{'widget':TinyMCE()}   #campo que vamos a cambiar.AVERIGUAR:formfield_overrides y 'widget'
  }


admin.site.register(Entradas,ProyectoAdmin) # el modelo a importar llamando entrada y ProyectoAdmin
admin.site.register(Contacto)
admin.site.register(EntradaDos,ProyectoAdmin)
admin.site.register(Servicios,ProyectoAdmin)


