# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Sede(models.Model):
    descripcion = models.CharField(max_length= 25, unique=True,
                                   verbose_name = "Descripción")

    def __unicode__(self):
        return self.descripcion
