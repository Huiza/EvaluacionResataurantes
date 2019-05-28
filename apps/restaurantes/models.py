from django.db import models

# Create your models here.

class Restaurante(models.Model):
	nombre_restaurante = models.CharField(max_length=50)
	direccion = models.CharField(max_length=50)
	telefono = models.CharField(max_length=10)
	nombre_encargado = models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.nombre_restaurante)


class Factor(models.Model):
	nombre_factor = models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.nombre_factor)

class Indicador(models.Model):
	nombre_indicador = models.CharField(max_length=50)
	factor = models.ForeignKey(Factor,null=True,blank=False,on_delete=models.CASCADE)

	def __str__(self):
		return '{}'.format(self.nombre_indicador)

class Evaluacion(models.Model):
	titulo = models.CharField(max_length=50)
	fecha = models.DateField()
	descripcion = models.CharField(max_length=500)
	nombre_inspector = models.CharField(max_length=50)
	comentarios = models.CharField(max_length=500)
	nota_final = models.IntegerField()
	restaurante = models.ForeignKey(Restaurante,null=True,blank=True,on_delete=models.CASCADE)

	def __str__(self):
		return '{}'.format(self.titulo,self.fecha,self.descripcion,self.nombre_inspector,self.comentarios)

class Resultado_Indicador(models.Model):
	evaluacion = models.ForeignKey(Evaluacion,null=True,blank=False,on_delete=models.CASCADE)
	indicador = models.ForeignKey(Indicador,null=True,blank=False,on_delete=models.CASCADE)
	nota_indicador = models.IntegerField()

	def __str__(self):
		return '{}'.format(self.nota_indicador)

class Resultado_Factor(models.Model):
	evaluacion = models.ForeignKey(Evaluacion,null=True,blank=False,on_delete=models.CASCADE)
	factor = models.ForeignKey(Factor,null=True,blank=False,on_delete=models.CASCADE)
	nota_factor = models.IntegerField()

	def __str__(self):
		return '{}'.format(self.nota_factor)
