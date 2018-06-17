# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from espaciofisico.models import Sede

# Create your models here.

class Recursos(models.Model):
    recursoTecnologico = models.BooleanField(default = True,
        verbose_name = "Recurso Tecnológico")
    disponibilidad = models.BooleanField(default = False,
        verbose_name = "Disponible")
    estadoBaja = models.BooleanField(default = False,
        verbose_name = "Baja de Activo")
    descripcion = models.CharField(max_length = 45, verbose_name = "Descripción")
    caracteristicas = models.TextField(blank = True, null = True)
    marca = models.CharField(max_length = 45, blank = True, null = True)
    modelo = models.CharField(max_length = 45, blank = True, null = True)
    numeroSerie = models.CharField(max_length = 45, blank = True,
        null = True, verbose_name = "Número de Serie")
    accesorios = models.TextField(blank = True, null = True)
    perifericos = models.TextField(blank = True, null = True,
        verbose_name="Periféricos")
    sede = models.ForeignKey(Sede, verbose_name="Sede")

    def __unicode__(self):
        return self.descripcion
