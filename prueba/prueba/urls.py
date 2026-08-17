"""
URL configuration for prueba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpattern  s:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings #Permite acceder a la svariables MEDIA_URL y MEDIA_ROOT que alamacenan la ubicacion de nuestras imagenes
from django.urls import path
from inicio.views import principal
from inicio.views import contacto
from inicio.views import formulario
from inicio.views import nombre
from inicio.views import ejemplo
from registros import views as views_registros


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_registros.registros, name="Principal"),
    # path('', principal, name='Principal'),
    path('nombre/', nombre, name='nombre'),
    path('contacto/', views_registros.contacto, name="contacto"),
    path('formulario/', formulario, name='formulario'),
    path('ejemplo/', ejemplo, name="ejemplo"),
    path('registrar/', views_registros.registrar, name="Registrar"),
    path('consultaContacto/', views_registros.consultaContacto, name="consultaContacto"),
    path('eliminarComentario/<int:id>/', views_registros.eliminarComentario, name='eliminar'),
    path('formEditarComentario/<int:id>/', views_registros.consultarComentarioIndividual, name='ConsultaIndividual'),
    path('editarComentario/<int:id>/', views_registros.editarComentarioContacto, name='editar'),
    path('consultas/', views_registros.consultas, name="consultas"),
    path('consultas1/', views_registros.consultar1, name="consultas1"),
    path('consultas2/', views_registros.consultar2, name="consultas2"),
    path('consultas3/', views_registros.consultar3, name="consultas3"),
    path('consultas4/', views_registros.consultar4, name="consultas4"),
    path('consultas5/', views_registros.consultar5, name="consultas5"),
    path('consultas6/', views_registros.consultar6, name="consultas6"),
    path('consultas7/', views_registros.consultar7, name="consultas7"),
    path('consultasSQL/', views_registros.consultasSQL, name="sql"),
    path('subir',views_registros.archivos,name="subir"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)
