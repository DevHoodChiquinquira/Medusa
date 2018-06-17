from django.contrib import admin
from .models import Recursos
# Register your models here.
@admin.register(Recursos)
class AdminRecursos(admin.ModelAdmin):
    list_display = ('descripcion', 'recursoTecnologico',)
    
