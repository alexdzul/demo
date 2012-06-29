from django.shortcuts import render_to_response
from django.template import RequestContext
from demo.apps.ventas.forms import addProductForm 
from demo.apps.ventas.models import producto


def add_product_view(request):
	if request.method == 'POST':
		form = addProductForm(request.POST)
		guardado = False
		info = "Inicia todo"
		if form.is_valid():
			
			nombre = form.cleaned_data['nombre']
			descripcion = form.cleaned_data['descripcion']
			p = producto()
			p.nombre = nombre
			p.descripcion = descripcion
			p.status = True
			p.save() # Guardamos el producto
			info = " Se guardo satisfactoriamente!!!!"
			guardado = True
		else:
			info = " No se pudo Guardar"
			form = addProductForm()
		ctx = {'form':form,'guardado':guardado,'informacion':info}
		return render_to_response('ventas/addProducto.html',ctx,context_instance=RequestContext(request))
	else:
		form = addProductForm()
		ctx = {'form':form}
		return render_to_response('ventas/addProducto.html',ctx,context_instance=RequestContext(request))
