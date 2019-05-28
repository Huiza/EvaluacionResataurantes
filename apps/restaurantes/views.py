from django.views.generic import CreateView,ListView,UpdateView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from apps.restaurantes.forms import *
from apps.restaurantes.models import *

# Create your views here.
class RestauranteList(ListView):
	model = Restaurante
	template_name = 'Restaurante/listaRestaurantes.html'

class RestauranteCreate(CreateView):
	model = Restaurante
	template_name ='Restaurante/nuevoRestaurante.html'
	form_class = RestauranteForm
	success_url = reverse_lazy('restaurante:listar_restaurantes')

class RestauranteUpdate(UpdateView):
	model = Restaurante
	template_name = 'Restaurante/nuevoRestaurante.html'
	form_class = RestauranteForm
	success_url = reverse_lazy('restaurante:listar_restaurantes')

def restauranteCrear(request):
	if not request.user.is_active:
			return redirect('/')
	us=request.user
	siembras = Siembra.objects.get(id=1)
	usuario_id = Usuario.objects.get(nombre_usuario=us)
	forms = SimulacionForm
	if request.method == 'POST':
		simula = Simulacion()
		confi = Configuracion()
		fase = FaseCultivo()
		#VALIDO LA ENTRADA, PARA CONOCER SI ES TRUE O FALSE
		fase.germinacion=True if request.POST.get('germinacion') else False
		fase.mergencia=True if request.POST.get('emergencia') else False
		fase.hojaPrimaria=True if request.POST.get('hojaPrimaria') else False
		fase.primeraHoja=True if request.POST.get('primeraHoja') else False
		fase.terceraHoja=True if request.POST.get('terceraHoja') else False
		fase.prefloracion=True if request.POST.get('prefloracion') else False
		fase.floracion=True if request.POST.get('floracion') else False
		fase.save()
		fase_id = FaseCultivo.objects.latest('id')
		
		confi.temperaturaMax = request.POST['temperaturaMax']
		confi.temperaturaMin = request.POST['temperaturaMin']
		confi.humedad = request.POST['humedad']
		confi.altitud = request.POST['altitud']
		confi.luminosidad = request.POST['luminosidad']
		confi.distanciaLinea = request.POST['distanciaL']
		confi.save() #guardar cambios de configuracion
		confi_id = Configuracion.objects.latest('id')

		simula.nombre = request.POST['simulacion']
		simula.lineaSiembra = request.POST['linea']
		simula.estado = 1
		simula.siembra = siembras
		simula.usuario = usuario_id
		simula.configuracion=confi_id
		simula.faseCultivo = fase_id
		simula.save() #guardar cambios de simulacion 
		return redirect('nuevo:simula')
	contexto = {'siembras':siembras}
	return render(request,'Simulacion/nuevo.html',contexto)

	
#def RestauranteEditar(request,id_restaurante):
#	restaurante =Restaurante.objects.get(id=id_restaurante)
#	if request.method=='GET':
#		form = RestauranteForm(instance=restaurante)
#
#	else:
#		form = RestauranteForm(request.POST,instance=restaurante)
#		if form.is_valid():
#			form.save()
#		return redirect('restaurante:listar_restaurantes')
#	return render(request,'Restaurante/nuevoRestaurante.html', {'form':form})




#def RestauranteEditar(request,id_restaurante):
#	if not request.user.is_active:
#			return redirect('/')
#			
#	restaurante = get_object_or_404(Restaurante,pk=id_restaurante)
 
3#	if request.method == 'POST':
#		restauranteElimina = restaurante.objects.get(id=id_restaurante)
#		restauranteElimina.delete()
#		restaurante = Restaurante() 
#		restaurante.nombre_restaurante = request.POST['nombre_restaurante']
#		restaurante.direccion = request.POST['direccion']
#		restaurante.telefono = request.POST['telefono']
#		restaurante.nombre_encargado = request.POST('nombre_encargado')
#		restaurante_id = Restaurante.objects.latest('id')
#		restaurante.id=restaurante_id
#		restaurante.save()
#
#		return redirect('restaurante:listar_restaurantes')
#	else:
#		contexto = {'restaurante':restaurante}
#		return render(request,'Restaurante/nuevoRestaurante.html',contexto)