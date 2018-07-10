#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Perfil, ProgramaAcademicoPerfil
from academia.models import ProgramaAcademico
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
from django.db.models import Q
# Create your views here.
@login_required()
def systemIndex(request):
    return render(request, 'system_index.html', {} )


#-----------------------Perfil------------------------#
class PerfilInsert(LoginRequiredMixin, CreateView):

    model = Perfil
    success_url = reverse_lazy('usuario:perfil_list')
    fields = ['numeroDocumento','telefono1', 'telefono2',
              'direccion', 'ciudad']
    success_url = reverse_lazy('usuario:perfil_list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(PerfilInsert, self).form_valid(form)

class PerfilList(LoginRequiredMixin, ListView):
    model = Perfil
    context_object_name = 'perfiles'
    def get_context_data(self, **kwargs):
        context = super(PerfilList, self). get_context_data(**kwargs)
        programa = ProgramaAcademicoPerfil.objects.filter(Q(programaacademico__estadoActivo=True),
                                                          Q(usuario=self.request.user))
        context.update({
            'programas':programa,
        })
        return context
#esta funcion permite ver solo las reservaciones del usuario
    def get_queryset(self):
        return Perfil.objects.filter(user=self.request.user)

class PerfilUpdate(LoginRequiredMixin, UpdateView):
    model = Perfil
    success_url = reverse_lazy('usuario:perfil_list')
    fields = ['numeroDocumento','telefono1', 'telefono2',
              'direccion', 'ciudad',]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PerfilUpdate, self).form_valid(form)


@login_required()
def perfil_detail(request, pk):
    perfil = get_object_or_404(Perfil, pk=pk)
    template = loader.get_template('usuario/perfil_detail.html')
    context = {
        'perfil' : perfil
    }
    return HttpResponse(template.render(context, request))
#-----------------END - Profile------------------

class ProgramaAcademicoPerfilInsert(LoginRequiredMixin, CreateView):

    model = ProgramaAcademicoPerfil
    success_url = reverse_lazy('usuario:perfil_list')
    fields = ['programaacademico',]

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(ProgramaAcademicoPerfilInsert, self).form_valid(form)
