from django.shortcuts import render
from .models import Alumnos, ComentarioContacto #Accedemos al modelo Alumnos que contiene la estructura de la tabla.
from.forms import ComentarioContactoForm

# Create your views here.
def registros(request):
    alumnos = Alumnos.objects.all() # all recuperar todos los objetos del modelo (registros de la tabla alumnos)
    
    return render(request, "registros/principal.html", {'alumnos': alumnos})
    #indicamso el lugar donde se renderiza el resultado de esta vista y enviamos la lista de alumnos recuperados

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            comentarios = ComentarioContacto.objects.all()
            return render(request, "registros/consultaContacto.html", {'comentarios': comentarios})
    form = ComentarioContactoForm()
    #si sale mal se reenvian al formulario de los datos ingresados
    return render(request,'registros/contacto.html', {'form': form})

def contacto(request):
    return render(request, "registros/contacto.html")
#Funcion de visualización del formulario
        
    
