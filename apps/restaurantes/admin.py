from django.contrib import admin

# Register your models here.
from apps.restaurantes.models import *

admin.site.register(Restaurante)
admin.site.register(Factor)
admin.site.register(Indicador)
admin.site.register(Evaluacion)
admin.site.register(Resultado_Indicador)#admin.site.register(Descuento)
admin.site.register(Resultado_Factor)