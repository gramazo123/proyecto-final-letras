from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.lista_letras),
    url(r'^banda/(?P<pk>[0-9]+)/$', views.detalles_banda),
    url(r'^banda/nueva/$', views.agregar_banda, name='agregar_banda'),
]

