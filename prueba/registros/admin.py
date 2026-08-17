from django.contrib import admin
from .models import Alumnos
from.models import comentario
from .models import ComentarioContacto



# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('matricula', 'nombre', 'carrera', 'turno','created')
    search_fields = ('matricula', 'nombre', 'carrera', 'turno')
    date_hierarchy = 'created'
    list_filter = ('carrera', 'turno')
   
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='usuario').exists():  # Editing an existing object
            return ('matricula','carrera','turno')
        elif request.user.groups.filter(name='grupovic').exists(): 
            return ('matricula','turno','created','updated')
        else:

         return('created','updated')
admin.site.register(Alumnos, AdministrarModelo)

class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id', 'coment')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
    ordering = ('-created',)
    list_filter = ('created',)
    list_display_links = ('coment',)

admin.site.register(comentario, AdministrarComentarios)

class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
admin.site.register(ComentarioContacto, AdministrarComentariosContacto)


