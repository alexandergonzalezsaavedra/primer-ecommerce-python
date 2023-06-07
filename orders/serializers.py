from .models import Categoria,Producto,Historial,OrdenCompra

from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import (
SerializerMethodField
)
from rest_framework import serializers

class CategoriasSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(ModelSerializer):
    categoriaProducto = CategoriasSerializer(many=True)
    class Meta:
        model = Producto
        fields = '__all__'