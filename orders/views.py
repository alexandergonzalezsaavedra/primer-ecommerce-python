from django.shortcuts import render
from .models import Categoria,Subcategoria,Producto,Historial,OrdenCompra
from rest_framework.generics import CreateAPIView,RetrieveUpdateAPIView,UpdateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView,DestroyAPIView
from .serializers import CategoriasSerializer,SubcategoriasSerializer,ProductoSerializer

# Create your views here.
# @permission_classes((AllowAny, ))

class categoryListApi(ListAPIView):
    serializer_class = CategoriasSerializer
    queryset = Categoria.objects.all().order_by('nombre')

class subcategoryListApi(ListAPIView):
    serializer_class = SubcategoriasSerializer
    queryset = Subcategoria.objects.all().order_by('nombreSubCategoria')

class productListApi(ListAPIView):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all().order_by('nombreProducto')
    # queryset = Producto.objects.filter(precioVentaProducto__lte=230, precioCompraProducto__gte=180)

# Ejemplos filtro
# queryset = Producto.objects.filter(precio__lte=5000000, precio__gte=1000000)
# queryset = generalModels.City.objects.all().order_by('name')