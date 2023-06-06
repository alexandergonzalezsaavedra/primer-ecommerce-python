from django.shortcuts import render
from .models import Categoria,Producto,Historial,OrdenCompra
from rest_framework.generics import CreateAPIView,RetrieveUpdateAPIView,UpdateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView,DestroyAPIView
from .serializers import ProductoSerializer,CategoriasSerializer

# Create your views here.
# @permission_classes((AllowAny, ))
class productListApi(ListAPIView):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all().order_by('nombreProducto')
    # queryset = Producto.objects.filter(precioVentaProducto__lte=230, precioCompraProducto__gte=180)

class categoryListApi(ListAPIView):
    serializer_class = CategoriasSerializer
    queryset = Categoria.objects.all().order_by('nombre')

# Ejemplos filtro
# queryset = Producto.objects.filter(precio__lte=5000000, precio__gte=1000000)
# queryset = generalModels.City.objects.all().order_by('name')