from .models import Categoria,Subcategoria,Producto,Historial,OrdenCompra

from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import (
SerializerMethodField
)
from rest_framework import serializers

class CategoriasSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class SubcategoriasSerializer(ModelSerializer):
    categoriaAsociada = CategoriasSerializer(many=False)
    class Meta:
        model = Subcategoria
        fields = '__all__'

class ProductoSerializer(ModelSerializer):
    subCategoriaProducto = SubcategoriasSerializer(many=True)
    class Meta:
        model = Producto
        fields = '__all__'