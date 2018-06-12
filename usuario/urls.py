
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="login.html"), name="login"),
    url(r'^plataforma', views.systemIndex, name="system_index"),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name="logout"),
]
