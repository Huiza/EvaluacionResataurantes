from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from apps.restaurantes.forms import *
from apps.restaurantes.models import *

# Create your views here.

class IndicadorList(ListView):
	model = Indicador
	template_name ='Restaurante/nuevaEvaluacion.html'

class EvaluacionCreate(CreateView):
	model = Evaluacion
	form_class = EvaluacionForm()
	success_url = reverse_lazy('restaurante:listar_restaurantes')

class ResultadoIndicador(CreateView):
	model = Resultado_Indicador
	form_class = ResultadoIndicadorForm()
	success_url= reverse_lazy('restaurante:listar_restaurantes')

class ResultadoFactor(CreateView):
	model = Resultado_Factor
	form_class = ResultadoFactorForm()
	success_url= reverse_lazy('restaurante:listar_restaurantes')

class EvaluacionList(ListView):
	model = Evaluacion
	template_name ='Restaurante/reportes.html'
