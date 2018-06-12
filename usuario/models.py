# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from espaciofisico.models import Sede
from academia.models import ProgramaAcademico, Grupo
from phonenumber_field.modelfields import PhoneNumberField

class Perfil(models.Model):
    numeroDocumento = models.CharField(max_length=20, unique=True,
        verbose_name=" Número de Documento")
    telefono1 = PhoneNumberField(default='+573040000000',
        verbose_name="Teléfono 1")
    telefono2 = PhoneNumberField(default='+573040000000',
        verbose_name="Teléfono 2")
    direccion = models.CharField(max_length=45, verbose_name="Dirección")
    ciudad = models.CharField(max_length=45, verbose_name="Ciudad")
    user = models.OneToOneField(User, verbose_name="Usuario")

    def __unicode__(self):
        return self.username

class ProgramaAcademicoPerfil(models.Model):
    usuario = models.ForeignKey(User, verbose_name="Usuario")
    programaacademico = models.ForeignKey(ProgramaAcademico,
        verbose_name="Programa Académico")

    def __unicode__(self):
        return u'%s %s'%(self.usuario , self.programaacademico)

class MatriculaGrupo(models.Model):
    usuario = models.ForeignKey(User, verbose_name="Usuario")
    grupo = models.ForeignKey(Grupo, verbose_name="Grupo")

    def __unicode__(self):
        return u'%s %s'%(self.usuario , self.grupo)
