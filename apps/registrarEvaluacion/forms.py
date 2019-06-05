from django import forms 
from apps.restaurantes.models import *

class EvaluacionForm(forms.ModelForm):
	class Meta:
		model = Evaluacion

		fields=[
		'titulo',
		'fecha',
		'descripcion',
		'nombre_inspector',
		'comentarios',
		'restaurante',
		'nota_final',
		]

		labels={
		'titulo': 'Titulo',
		'fecha':'Fecha',
		'descripcion':'Descripción',
		'nombre_inspector':'Nombre inspector',
		'comentarios':'Comentarios',
		'restaurante': 'Restaurante',
		'nota_final':' Nota final',
		}

		widgets={
		'titulo':forms.TextInput(attrs={'class':'form-control'}),
		'fecha':forms.TextInput(attrs={'class':'form-control'}),
		'descripcion':forms.TextInput(attrs={'class':'form-control'}),
		'nombre_inspector':forms.TextInput(attrs={'class':'form-control'}),
		'comentarios':forms.TextInput(attrs={'class':'form-control'}),
		'restaurante':forms.Select(attrs={'class':'form-control'}),		
		'nota_final':forms.TextInput(attrs={'class':'form-control'}),
		}
class ResultadoIndicadorForm(forms.ModelForm):
	class Meta:
		model = Resultado_Indicador

		fields=[
		'evaluacion',
		'indicador',
		'nota_indicador',
		]

		labels={
		'evaluacion':'Evaluacion',
		'indicador':'Indicador',
		'nota_indicador': 'Calificacion',
		}


		widgets={
		'evaluacion':forms.Select(attrs={'class':'form-control'}),
		'indicador': forms.Select(attrs={'class':'form-control'}),
		'nota_indicador':forms.TextInput(attrs={'class':'form-control'}),
		}

class ResultadoFactorForm(forms.ModelForm):
	class Meta:
		model = Resultado_Factor

		fields=[
		'nota_factor',
		]

		labels={
		'nota_factor': 'Calificacion',
		}


		widgets={
		'nota_factor':forms.TextInput(attrs={'class':'form-control'}),
		}
