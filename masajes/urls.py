from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.lista_cliente, name ='lista_cliente'),
    url(r'^cliente/nueva/$', views.cliente_nueva, name='cliente_nueva'),
    url(r'^cliente/(?P<pk>[0-9]+)/editar/$', views.cliente_edit, name='cliente_edit'),
    url(r'^cliente/(?P<pk>\d+)/remove/$', views.cliente_remove, name='cliente_remove'),
    url(r'^Empleado/nueva/$', views.Empleada_nueva, name='Empleada_nueva'),
    url(r'^Empleado/Listar/$', views.Empleado_listar, name='Empleado_listar'),
    url(r'^Empleado/(?P<pk>[0-9]+)/editar/$', views.Empleado_edit, name='Empleado_edit'),
    url(r'^Empleado/(?P<pk>\d+)/remove/$', views.Empleado_remove, name='Empleado_remove'),
    #url(r'^post/new/$', views.post_new, name='post_new'),
    #url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    #url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    #url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    #url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove')
    ]
