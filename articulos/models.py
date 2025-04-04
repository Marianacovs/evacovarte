from django.db import models
from django.core.validators import RegexValidator

#los modelos son las entradas dentro del administrador y nos permiten interectuar con la base de datos.
#se crean mediante clases y estas tiene herencias de clases(lo que esta dentro del parentesis y esta invocado arriba)

#modificacion de tabla:siempre hay que realizar una nueva migracion si hay una modificacion.
#OJO ESTO ES SUPER IMPORTANTE
class Entradas(models.Model):
    nombre=models.CharField(max_length=200,null=True, blank=True)
    contenido=models.TextField(max_length=2000,null=True, blank=True)                                             
    autor=models.CharField(max_length=50,null=True, blank=True)
    imagen=models.ImageField(upload_to='productos', blank=True,null=True) #  se guarda en la carpeta de media y no en la base de datos django
 

    def __str__(self):         # esto para que se vean en el titulo del campos del formulario,PERO NECESITO UNO VACIO POR ESO LO MODIFIQUE
       if self.nombre is not None:return str(self.nombre) 
       else: return "introduccion,solo imagen o logo" 
       

class EntradaDos(models.Model):
    nombre=models.CharField(max_length=200,null=True, blank=True)
    contenido=models.TextField(max_length=2000,null=True, blank=True)                                             
    autor=models.CharField(max_length=50,null=True, blank=True)
    imagen=models.ImageField(upload_to='productos', blank=True,null=True) #  se guarda en la carpeta de media y no en la base de datos django
 

    def __str__(self):         # esto para que se vean en el titulo del campos del formulario,PERO NECESITO UNO VACIO POR ESO LO MODIFIQUE
       if self.nombre is not None:return str(self.nombre) 
       else: return "introduccion,solo imagen o logo" 
    
# formulario Django:
class Contacto(models.Model):
    # Validador que permite solo letras (mayúsculas y minúsculas)
    solo_letras = RegexValidator(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', 'Solo se admiten letras')

    nombre=models.CharField(max_length=100,validators=[solo_letras])
    correo=models.EmailField()
    mensaje=models.TextField()
    avisos=models.BooleanField()

    def __str__(self):        
        return self.nombre
    
#servicios:
class Servicios(models.Model):
    nombre=models.CharField(max_length=200,null=True, blank=True)
    contenido=models.TextField(max_length=2000,null=True, blank=True)                                             
    autor=models.CharField(max_length=50,null=True, blank=True)
    imagen=models.ImageField(upload_to='productos', blank=True,null=True) #  se guarda en la carpeta de media y no en la base de datos django

    def __str__(self):         # esto para que se vean en el titulo del campos del formulario,PERO NECESITO UNO VACIO POR ESO LO MODIFIQUE
       if self.nombre is not None:return str(self.nombre) 
       else: return "introduccion,solo imagen o logo" 
 