# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
urlpatterns = [
    url(r'^recursos/new', views.RecursoInsert.as_view(), name="recursos_insert"),
    url(r'^recurso/list$',views.RecursoList.as_view(), name='recursos_list'),
    # url(r'^perfil/edit(?P<pk>[0-9]+)/$',views.PerfilUpdate.as_view(),
    # 	name='perfil_edit'),
    # url(r'^(?P<pk>[0-9]+)/$', views.perfil_detail,
	# 	name="perfil_detail")
]
