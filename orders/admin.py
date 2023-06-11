from django.contrib import admin
from .models import Categoria,Subcategoria,Producto,Historial,OrdenCompra
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Subcategoria)
admin.site.register(Producto)
admin.site.register(Historial)
admin.site.register(OrdenCompra)