from django.shortcuts import render
from articulos.models import Entradas  #mandando diccionarios.de la app articulos importa el modelo entrada
from.forms import ContactoForm
from articulos.models import EntradaDos,Servicios


def home(request):
    return render(request, 'home.html')  # Asegúrate de que la plantilla existe.MIRAR PORQ ESTA DOBLE

#si acceden a home trae al archivo html
def home(request):
    articulos=Entradas.objects.all()   #del modelo de entrada se guarda en articulos y se envian a traves de diccionarios
    return render(request,'bienvenida.html',{'articulos':articulos})

#Para importar el modelo del formulario aqui
def contacto(request):
    data={
        'form':ContactoForm()
    }
    if request.method== 'POST':
        formulario=ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']='Contacto guardado'
        else:
            data['form']=formulario        # esto para que vuelva aparecer el formulario y volver a llenar

    return render(request,'contacto.html',data)


def nosotros(request):
    articulos=EntradaDos.objects.all()   #del modelo de entrada se guarda en articulos y se envian a traves de diccionarios
    return render(request,'nosotros.html',{'articulos':articulos})

# def nosotros(request):
#     return render(request,'nosotros.html',)

def base(request):
    return render(request,'base.html')

def servicios(request):
    articulos=Servicios.objects.all()   #del modelo de entrada se guarda en articulos y se envian a traves de diccionarios
    return render(request,'servicios.html',{'articulos':articulos})
