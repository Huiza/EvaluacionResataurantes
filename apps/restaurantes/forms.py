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
		]

		labels={
		'titulo': 'Titulo',
		'fecha':'Fecha',
		'descripcion':'Descripción',
		'nombre_inspector':'Nombre inspector',
		'comentarios':'Comentarios',
		'restaurante': 'Restaurante',
		}


		widgets={
		'titulo':forms.TextInput(attrs={'class':'form-control'}),
		'fecha':forms.TextInput(attrs={'class':'form-control'}),
		'descriwpcion':forms.TextInput(attrs={'class':'form-control'}),
		'nombre_inspector':forms.TextInput(attrs={'class':'form-control'}),
		'comentarios':forms.TextInput(attrs={'class':'form-control'}),
		'restaurante':forms.Select(attrs={'class':'form-control'}),		
		}

class RestauranteForm(forms.ModelForm):
	class Meta:
		model = Restaurante

		fields=[
		'nombre_restaurante',
		'direccion',
		'telefono',
		'nombre_encargado',
		]

		labels={
		'nombre_restaurante': 'Nombre restaurante',
		'direccion':'Dirección',
		'telefono':'Teléfono',
		'nombre_encargado':'Nombre encargado',
		}


		widgets={
		'nombre_restaurante':forms.TextInput(attrs={'class':'form-control'}),
		'direccion':forms.TextInput(attrs={'class':'form-control'}),
		'telefono':forms.TextInput(attrs={'class':'form-control'}),
		'nombre_encargado':forms.TextInput(attrs={'class':'form-control'}),	
		}

class ResultadoIndicadorForm(forms.ModelForm):
	class Meta:
		model = Resultado_Indicador

		fields=[
		'nota_indicador',
		]

		labels={
		'nota_indicador': 'Calificacion',
		}


		widgets={
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