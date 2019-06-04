from django.conf.urls import url,include
from django.contrib import admin

from apps.restaurantes.views  import *
#reservacion_view,cliente_view,RegistroReservacion
app_name='restaurantes'

urlpatterns = [
     url(r'^nuevo/$', RestauranteCreate.as_view(), name='nuevo'),
     #url(r'^editar/(?P<id_restaurante>\d+)/$', RestauranteEditar, name='editar'),
     url(r'^editar/(?P<pk>\d+)/$',RestauranteUpdate.as_view(), name='editar'),
     url(r'^listar/$', RestauranteList.as_view(), name='listar_restaurantes'),
  
]
from django.conf.urls import url,include
from apps.restaurantes.views import index

urlpatterns = [
    url(r'^$', index),
    
    
]