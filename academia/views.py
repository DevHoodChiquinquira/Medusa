#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import (Facultad, ProgramaAcademico,
                     Asignatura, Grupo)
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
import json
import decimal
from django.core import serializers
from django.template import RequestContext
from django.db import transaction
from django.contrib import messages
from django.template import RequestContext as ctx
from django.template import Context
from .forms import RangoForm
from django.utils import timezone

class FacultadInsert(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    permission_required = ('academia.add_facultad')
    model = Facultad
    success_url = reverse_lazy('academia:facultad_list')
    fields = ['descripcion', ]

class FacultadList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = ('academia.change_facultad')
    model = Facultad
    context_object_name = 'facultades'

class FacultadUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    permission_required = ('academia.add_facultad')
    model = Facultad
    success_url = reverse_lazy('academia:facultad_list')
    fields = ['descripcion', ]

class ProgramaAcademicoInsert(LoginRequiredMixin,
                              PermissionRequiredMixin, CreateView):
    permission_required = ('academia.add_programaacademico')
    model = ProgramaAcademico
    success_url = reverse_lazy('academia:programa_academico_list')
    fields = ['estadoActivo', 'codigo', 'descripcion',
              'nivelformacion', 'facultad', 'sede', 'registroCalificado',]

class ProgramaAcademicoList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = ('academia.change_programaacademico')
    model = ProgramaAcademico
    context_object_name = 'programas'

class ProgramaAcademicoUpdate(LoginRequiredMixin,
    PermissionRequiredMixin, UpdateView):
    permission_required = ('academia.add_programaacademico')
    model = ProgramaAcademico
    success_url = reverse_lazy('academia:programa_academico_list')
    fields = ['estadoActivo', 'codigo', 'descripcion',
              'nivelformacion', 'facultad', 'sede', 'registroCalificado',]

@login_required()
def programa_academico_detail(request, pk):
    programa = get_object_or_404(ProgramaAcademico, pk=pk)
    template = loader.get_template('academia/programaacademico_detail.html')
    context = {'programa' : programa}
    return HttpResponse(template.render(context, request))

class AsignaturaInsert(LoginRequiredMixin,
                       PermissionRequiredMixin, CreateView):
    permission_required = ('academia:add_asignatura')
    model = Asignatura
    success_url = reverse_lazy('academia:asignatura_list')
    fields = ['estado_activo', 'descripcion', 'programaacademico']

class AsignaturaList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = ('academia:add_asignatura')
    model = Asignatura
    context_object_name = 'asignaturas'

class AsignaturaUpdate(LoginRequiredMixin,
                       PermissionRequiredMixin, UpdateView):
    permission_required = ('academia:add_asignatura')
    model = Asignatura
    success_url = reverse_lazy('academia:asignatura_list')
    fields = ['estado_activo', 'descripcion', 'programaacademico']

class GrupoInsert(LoginRequiredMixin,
                       PermissionRequiredMixin, CreateView):
    permission_required = ('academia:add_grupo')
    model = Grupo
    success_url = reverse_lazy('academia:asignatura_list')
    fields = ['estado_activo', 'descripcion', 'user']



def grupoInsert (request):
    form = None
    if request.method == 'POST':
        sid = transaction.savepoint()
        try:
            #algoritmo
            pass

        except Exception, e:
            try:
                transaction.savepoint_rollback(sid)
            except:
                pass
            messages.error(request,e)
    return render(request, 'academia/Grupo_Asignatura.html')


def serachAsignatura(request):
    asig_nombre = request.GET.get('NombreAsignatura')
    asig_cons = Asignatura.objects.filter(descripcion__icontains=asig_nombre)
    asig_cons = [asignatura_serializer(asignatura) for asignatura in asig_cons]
    return HttpResponse(json.dumps(asig_cons), content_type='application/json')

def asignatura_serializer(asignatura):
    return{'id':asignatura.id, 'descripcion':asignatura.descripcion,
           'estado_activo': asignatura.estado_activo,
           'programaacademico': asignatura.programaacademico.id,
           'programaacademico__descripcion':asignatura.programaacademico.descripcion}
