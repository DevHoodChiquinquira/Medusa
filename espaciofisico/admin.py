from django.contrib import admin
from .models import Sede
# Register your models here.
@admin.register(Sede)
class AdminSede(admin.ModelAdmin):
    list_display =('id','descripcion',)
