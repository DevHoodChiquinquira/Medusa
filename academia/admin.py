from django.contrib import admin
from academia.models import Facultad, ProgramaAcademico, Asignatura, Grupo, GrupoAsignatura

@admin.register(Facultad)
class AdminFacultad(admin.ModelAdmin):
    list_display = ('descripcion',)

@admin.register(ProgramaAcademico)
class AdminFacultad(admin.ModelAdmin):
    list_display = ('codigo', 'descripcion', 'sede', 'facultad',)

@admin.register(Asignatura)
class AdminAsignatura(admin.ModelAdmin):
    list_display = ('descripcion', 'estado_activo', 'programaacademico',)

@admin.register(Grupo)
class AdminGrupo(admin.ModelAdmin):
    list_display = ('descripcion', 'estado_activo', 'user',)

@admin.register(GrupoAsignatura)
class AdminGrupoAsignatura(admin.ModelAdmin):
    list_display = ('grupo', 'asignatura',)
