# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from espaciofisico.models import Sede
from django.contrib.auth.models import User

class Facultad(models.Model):
    descripcion = models.CharField(max_length = 50, unique = True,
        verbose_name = "Descripción")
    def __unicode__(self):
        return self.descripcion

class ProgramaAcademico(models.Model):
    NIVEL_FORMACION = (
        ('posgrado', 'Posgrado'),
        ('pregrado', 'Pregrado'),
        ('administrativo', 'Administrativo'),
    )
    estadoActivo = models.BooleanField(default=True, verbose_name = "Activo")
    codigo = models.CharField(max_length=25, unique=True, verbose_name="Código SNIES")
    descripcion = models.CharField(max_length=50)
    nivelformacion = models.CharField(choices=NIVEL_FORMACION,
        max_length= 50, verbose_name="Nivel de formación")
    sede = models.ForeignKey(Sede, verbose_name= "Sede")
    facultad = models.ForeignKey(Facultad, verbose_name= "Facultad" )
    registroCalificado = models.TextField(max_length=200,
        blank=True, null=True, verbose_name="Registro Calificado",
        help_text='200 caracteres')

    def __unicode__(self):
        return u'%s %s %s'%(self.codigo, self.sede, self.descripcion)


class Asignatura(models.Model):
    descripcion = models.CharField(max_length= 50, verbose_name= "Descripción")
    estado_activo = models.BooleanField(default=True)
    programaacademico = models.ForeignKey(ProgramaAcademico,
        verbose_name = "Programa Académico")
    def __unicode__(self):
        return u'%s %s'%(self.descripcion , self.programaacademico)

class Grupo(models.Model):
    descripcion = models.CharField(max_length=25, verbose_name= "Grupo", unique=True)
    estado_activo = models.BooleanField(default=True)
    user = models.ForeignKey(User, verbose_name="Usuario")
    def __unicode__(self):
        return u'%s'%(self.descripcion)

class GrupoAsignatura(models.Model):
    grupo = models.ForeignKey(Grupo, verbose_name= "Grupo")
    asignatura = models.ForeignKey(Asignatura,
        verbose_name="Asignatura")
    def __unicode__(self):
        return u'%s %s'%(self.grupo , self.asignatura)
