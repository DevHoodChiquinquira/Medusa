
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="login.html"), name="login"),
    url(r'^plataforma', views.systemIndex, name="system_index"),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name="logout"),
    url(r'^perfil/new', views.PerfilInsert.as_view(), name="perfil_insert"),
    url(r'^perfil/list$',views.PerfilList.as_view(), name='perfil_list'),
    url(r'^perfil/edit(?P<pk>[0-9]+)/$',views.PerfilUpdate.as_view(),
    	name='perfil_edit'),
    url(r'^(?P<pk>[0-9]+)/$', views.perfil_detail,
		name="perfil_detail"),
]
