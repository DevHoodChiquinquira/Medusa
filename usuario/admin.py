from django.contrib import admin
from .models import Perfil
# Register your models here.
@admin.register(Perfil)
class AdminPerfil(admin.ModelAdmin):
    list_display = ('user', 'numeroDocumento','telefono1',)