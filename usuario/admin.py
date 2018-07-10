from django.contrib import admin
from .models import Perfil, ProgramaAcademicoPerfil
# Register your models here.
@admin.register(Perfil)
class AdminPerfil(admin.ModelAdmin):
    list_display = ('user', 'numeroDocumento','telefono1',)

@admin.register(ProgramaAcademicoPerfil)
class AdminProgramaAcademicoPerfil(admin.ModelAdmin):
    list_display = ('usuario', 'programaacademico',)
