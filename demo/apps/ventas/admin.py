from django.contrib	import admin
from demo.apps.ventas.models import cliente,producto,categoriaProducto

admin.site.register(cliente)
admin.site.register(producto)
admin.site.register(categoriaProducto)
