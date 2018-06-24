from django.contrib import admin
from .models import Recursos, ReservacionLugar, ComentarioReservacionLugar
# Register your models here.
@admin.register(Recursos)
class AdminRecursos(admin.ModelAdmin):
    list_display = ('descripcion', 'recursoTecnologico',)

@admin.register(ReservacionLugar)
class AdminReservacionLugar(admin.ModelAdmin):
    list_display = ('descripcion', 'usuario', 'docente',)

@admin.register(ComentarioReservacionLugar)
class AdminComentarioReservacionLugar(admin.ModelAdmin):
    list_display = ('reservacionLugar', 'usuario',)
