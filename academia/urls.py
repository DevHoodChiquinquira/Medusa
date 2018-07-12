# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
urlpatterns = [
    url(r'^facultad/new', views.FacultadInsert.as_view(), name="facultad_insert"),
    url(r'^facultad/list$',views.FacultadList.as_view(), name='facultad_list'),
    url(r'^facultad/edit(?P<pk>[0-9]+)/$',views.FacultadUpdate.as_view(),
    	name='facultad_edit'),
    url(r'^progAcadem/new', views.ProgramaAcademicoInsert.as_view(),
        name="programa_academico_insert"),
    url(r'^progAcadem/list$',views.ProgramaAcademicoList.as_view(),
        name='programa_academico_list'),
    url(r'^progAcadem/edit(?P<pk>[0-9]+)/$',
        views.ProgramaAcademicoUpdate.as_view(),name='programa_academico_edit'),
    url(r'^progAcadem/detalle/(?P<pk>[0-9]+)/$',
        views.programa_academico_detail, name="programaacademico_detail"),
    url(r'^asignatura/new', views.AsignaturaInsert.as_view(),
        name="asignatura_insert"),
    url(r'^asignatura/list$',views.AsignaturaList.as_view(),
        name='asignatura_list'),
    url(r'^asignatura/edit(?P<pk>[0-9]+)/$',
        views.AsignaturaUpdate.as_view(),name='asignatura_edit'),
]
