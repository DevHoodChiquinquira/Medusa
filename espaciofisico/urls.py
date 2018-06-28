#-*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
urlpatterns = [
	url(r'^new', views.SedeInsert.as_view(), name="sede_insert"),
    url(r'^list$', views.SedeList.as_view(),name='sede_list'),
    url(r'^edit(?P<pk>[0-9]+)/$', views.SedeUpdate.as_view(),
    	name='sede_edit'),

]
