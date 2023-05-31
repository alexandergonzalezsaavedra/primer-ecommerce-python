from .models import Categoria,Producto,Historial,OrdenCompra

from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import (
SerializerMethodField
)
from rest_framework import serializers



class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'