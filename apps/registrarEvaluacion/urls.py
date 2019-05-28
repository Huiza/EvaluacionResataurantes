from django.conf.urls import url,include
from django.contrib import admin

from apps.registrarEvaluacion.views  import *
#reservacion_view,cliente_view,RegistroReservacion
app_name='registrarEvaluacion'

urlpatterns = [
     url(r'^listar/$', IndicadorList.as_view(),name='listar_indicadores'),
     url(r'^listar_evaluaciones/$', EvaluacionList.as_view(),name='listar_evaluaciones'),
     #url(r'^editar/(?P<id_restaurante>\d+)/$', RestauranteEditar, name='editar'),
     #url(r'^editar/(?P<pk>\d+)/$',RestauranteUpdate.as_view(), name='editar'),
 #    u3rl(r'^listar/$', RestauranteList.as_view(), name='listar_restaurantes'),
  
]
