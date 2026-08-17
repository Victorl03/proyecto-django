import datetime

from django.shortcuts import get_object_or_404, render
from httpx import request
from .models import Alumnos, ComentarioContacto #Accedemos al modelo Alumnos que contiene la estructura de la tabla.
from .forms import ComentarioContactoForm
from django.shortcuts import get_object_or_404
from .models import Archivos
from .forms import FormArchivos
from django.contrib import messages


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

def consultaContacto(request):
    comentarios = ComentarioContacto.objects.all()
    return render(request, "registros/consultaContacto.html", {'comentarios': comentarios})

def contacto(request):
    return render(request, "registros/contacto.html")
#Funcion de visualización del formulario
def eliminarComentario(request,id,confirmacion='registros/confirmarEliminacion.html'):
    comentario= get_object_or_404(ComentarioContacto, id=id)
    if request.method=='POST':
        comentario.delete()
        comentarios = ComentarioContacto.objects.all()
        return render(request, "registros/consultaContacto.html", 
    {'comentarios': comentarios})
    return render(request, confirmacion, {'object': comentario})

def consultarComentarioIndividual (request,id):
    comentario=ComentarioContacto.objects.get(id=id)
    #get permite establecer una condicionante a la consulta y recupera el objeto
    #del modelo que cumple la condicion (registro de la tabla ComentariosContacto.
    #get se emplea cuando se sabe que solo hay un objeto que concide con su
    #consulta
    return render(request,"registros/confirmarEdicion.html", {'comentario':comentario})

def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)
    #Referenciamos que el elemento del formulario pertenece al comentario
    # #ya existente
    if form.is_valid():
        form.save()#si el registro ya existe,se modifica.
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/consultaContacto.html",{'comentarios':comentarios})
    #si el formulario no es valido nos regresa al formulario para verificar
    # #datos
    return render(request,"registros/confirmarEdicion.html",{'comentario':comentario})     

def consultas(request):
    alumnos = Alumnos.objects.all() # all recuperar todos los objetos del modelo (registros de la tabla alumnos)
    return render(request, "inicio/consultas.html", {'alumnos': alumnos})

#funcion filter: filter nos retornara los registros que considen con los parametros de busqyeda datos


def consultar1(request):
    alumnos=Alumnos.objects.filter(carrera="TI")
    return render(request, "inicio/consultas.html", {'alumnos': alumnos})

def consultar2(request):
    alumnos=Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    return render(request, "inicio/consultas.html", {'alumnos': alumnos})

def consultar3(request):
    alumnos=Alumnos.objects.all().only("matricula","nombre","carrera","turno","imagen")
    return render(request, "inicio/consultas.html", {'alumnos': alumnos})

def consultar4(request):
    alumnos = Alumnos.objects.filter(carrera__in=["TI", "Bio"])
    return render(request, "inicio/consultas.html", {'alumnos': alumnos})

def consultar5(request):
    alumnos = Alumnos.objects.filter(nombre__startswith="A")
    return render(request, "inicio/consultas.html", {'alumnos': alumnos})

def consultar6(request):
    fechaInicio = datetime.date(2026,6, 20)
    fechaFin = datetime.date(2026,8, 4)
    alumnos=Alumnos.objects.filter(created__range=(fechaInicio, fechaFin))
    return render(request, "inicio/consultas.html", {'alumnos': alumnos})

def consultar7(request):
    #consultando entre modelos
    alumnos = Alumnos.objects.filter(comentario__coment__contains='alum')
    return render(request, "inicio/consultas.html", {'alumnos': alumnos})

def consultasSQL(request):
    alumnos=Alumnos.objects.raw('select id, matricula,nombre,carrera,turno,imagen FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC')
    return render(request,"inicio/consultas.html", {'alumnos': alumnos})


def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.POST,request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivo']
            insert =Archivos( titulo = titulo, descripcion = descripcion, archivo = archivo )
            insert.save()
            return render(request, "registros/archivos.html")
        else:
            messages.error(request,"Error al procesar el formulario")
    else:
        return render(request, "registros/archivos.html", {'archivo':Archivos})        



    
