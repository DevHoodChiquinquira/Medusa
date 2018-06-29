# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from espaciofisico.models import Sede
from academia.models import Grupo


# Create your models here.

class Recursos(models.Model):
    recursoTecnologico = models.BooleanField(default = False,
        verbose_name = "Recurso Tecnológico")
    disponibilidad = models.BooleanField(default = False,
        verbose_name = "Disponible")
    estadoBaja = models.BooleanField(default = False,
        verbose_name = "Baja de Activo")
    descripcion = models.CharField(max_length = 45, verbose_name = "Descripción")
    caracteristicas = models.TextField(max_length = 1000, blank = True,
        null = True, help_text='1.000 caracteres')
    marca = models.CharField(max_length = 45, blank = True, null = True)
    modelo = models.CharField(max_length = 45, blank = True, null = True)
    numeroSerie = models.CharField(max_length = 45, blank = True,
        null = True, verbose_name = "Número de Serie")
    placaInventario= models.CharField(max_length = 45, blank = True,
        null = True, verbose_name = "Placa de Inventario")
    accesorios = models.TextField(max_length = 1000, blank = True,
        null = True, help_text='1.000 caracteres')
    perifericos = models.TextField(max_length = 3000, blank = True,
        null = True, verbose_name="Periféricos",
        help_text='3.000 caracteres')
    sede = models.ForeignKey(Sede, verbose_name="Sede")

    def __unicode__(self):
        return self.descripcion


class ReservacionLugar(models.Model):
    descripcion = models.CharField(max_length=45, verbose_name = "Descripción",
        help_text='Nombre de la reservación, máximo 45 caracteres')
    fechaReserva = models.DateTimeField(auto_now_add = True,
        verbose_name="Fecha de Reservación")
    fechaInicio = models.DateTimeField(auto_now = False,
        verbose_name="Fecha de Inicio")
    fechaFinalizacion = models.DateTimeField(auto_now = False,
        verbose_name = "Fecha de Finalización")
    usuario = models.ForeignKey(User, verbose_name = "Usuario")
    docente = models.ForeignKey(User, verbose_name = "Docente",
        related_name="reservacionlugar_docente") #related_name permite diferenciar entre usuario y docente - recursion
    funcionario = models.ForeignKey(User, verbose_name="Funcionario",
        related_name="reservacionlugar_Funcionario",
        blank = True, null = True,
        help_text='Funcionario que da cierre a prestamo')
    observacionSolicitud = models.TextField(max_length = 1000,
        verbose_name = "Observación Solicitud", help_text='1.000 caracteres',
        blank = True, null = True)
    grupo = models.ForeignKey(Grupo, verbose_name = "Grupo")
    estadoActivo = models.BooleanField(default=True)
    Lugar = models.ForeignKey(Recursos, verbose_name = "Lugar")

    def __unicode__(self):
        return self.descripcion


class ComentarioReservacionLugar(models.Model):
    reservacionLugar = models.ForeignKey(ReservacionLugar,
        verbose_name="Reservación de Lugar")
    usuario = models.ForeignKey(User, verbose_name = "Usuario")
    comentario = models.TextField(max_length = 500,
        verbose_name = "Comentario", help_text='500 caracteres',
        blank = True, null = True)
    def __unicode__(self):
        return self.usuario



# class ReservacionRecursoTecnologico(models.Model):
#     estadoActivo = models.BooleanField(default=True)
#     reservacion = models.ForeignKey(ReservacionLugar,
#         verbose_name="Reservación")
#     recurso = models.ForeignKey(Recursos, verbose_name="Recurso")
#     usuario = models.ForeignKey(User, verbose_name="Solicitante")
#     funcionario = models.ForeignKey(User, verbose_name="Funcionario",
#         related_name="reservacionrecursotecnologico_Funcionario",
#         blank = True, null = True)
#     observacionSolicitud = models.TextField(max_length = 1000,
#         verbose_name = "Observación Solicitud", help_text='1.000 caracteres',
#         blank = True, null = True)
#     observacionEntrega = models.TextField(max_length = 1000,
#         verbose_name = "Observación Entrega", help_text='1.000 caracteres',
#         blank = True, null = True)
#     observacionRecepcion = models.TextField(max_length=1000,
#         verbose_name="Observación Recepción", help_text='1.000 caracteres',
#         blank = True, null = True)
