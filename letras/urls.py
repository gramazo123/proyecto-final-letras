from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.lista_letras),
    url(r'^banda/(?P<pk>[0-9]+)/$', views.detalles_banda),
    url(r'^banda/nueva/$', views.agregar_banda, name='agregar_banda'),
    url(r'^banda/(?P<pk>[0-9]+)/editar/$', views.editar_banda, name='editar_banda'),
    url(r'^letra/(?P<pk>[0-9]+)/$', views.detalles_cancion),
    url(r'^letra/nueva/$', views.agregar_letrasb, name='agregar_letrasb'),
    url(r'^banda/(?P<pk>[0-9]+)/letra/nueva/$', views.agregar_letras, name='agregar_letras'),
]

