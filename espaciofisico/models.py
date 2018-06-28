# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Sede(models.Model):
    descripcion = models.CharField(max_length= 25, unique=True,
                                   verbose_name = "Descripción")
    estadoActivo = models.BooleanField(default=True,
        verbose_name = "Estado Activo")

    def __unicode__(self):
        return self.descripcion
