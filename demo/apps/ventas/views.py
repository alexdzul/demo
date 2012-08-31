from django.shortcuts import render_to_response
from django.template import RequestContext
from demo.apps.ventas.forms import addProductForm
from demo.apps.ventas.models import producto
from django.http import HttpResponseRedirect

def add_product_view(request):
	info = "Inicializando" 
	if request.user.is_authenticated():
		if request.method == "POST":
			form = addProductForm(request.POST)
			if form.is_valid():
				nombre = form.cleaned_data['nombre']
				descripcion = form.cleaned_data['descripcion']
				p = producto()
				p.nombre =  nombre
				p.descripcion = descripcion
				p.status = True
				p.save() # Guardar la informacion
				info = "Se guardo satisfactoriamente!!!!!"
			else:
				info = "informacion con datos incorrectos"			
		form = addProductForm()
		ctx = {'form':form, 'informacion':info}
		return render_to_response('ventas/addProducto.html',ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')
