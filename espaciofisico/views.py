#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Sede
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


class SedeInsert(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
	permission_required = ('espaciofisico.add_sede')
	model = Sede
	success_url = reverse_lazy('espaciofisico:sede_list')
	fields = ['descripcion', 'estadoActivo' ]

class SedeList(LoginRequiredMixin, ListView):
    model = Sede
    context_object_name = 'sedes'

class SedeUpdate(LoginRequiredMixin,
                       PermissionRequiredMixin, UpdateView):
    permission_required = ('espaciofisico.change_sede')
    model = Sede
    success_url = reverse_lazy('espaciofisico:sede_list')
    fields = ['descripcion', 'estadoActivo']
