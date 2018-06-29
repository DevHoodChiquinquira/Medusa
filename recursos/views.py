#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Recursos
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    UpdateView,
    CreateView,
    DeleteView
    )
from django.core.urlresolvers import reverse_lazy
#mixins
from django.contrib.auth.mixins import(
    LoginRequiredMixin, PermissionRequiredMixin)
from django.contrib.auth.decorators import (
    login_required, permission_required)

class RecursoInsert(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    permission_required = ('recursos.add_recursos')
    model = Recursos
    success_url = reverse_lazy('recursos:recursos_list')
    fields = ['recursoTecnologico','disponibilidad','sede',
              'descripcion',  'marca', 'modelo', 'placaInventario',
              'numeroSerie', 'caracteristicas','accesorios', 'perifericos' ]

class RecursoList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = ('recursos.change_recursos')
    model = Recursos
    context_object_name = 'recursos'
#esta funcion permite ver solo las reservaciones del usuario
    # def get_queryset(self):
    #     return Perfil.objects.filter(user=self.request.user)

class RecursoUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    permission_required = ('recursos.add_recursos')
    model = Recursos
    success_url = reverse_lazy('recursos:recursos_list')
    fields = ['recursoTecnologico','disponibilidad','sede',
              'descripcion',  'marca', 'modelo', 'placaInventario',
              'numeroSerie', 'caracteristicas','accesorios', 'perifericos' ]
