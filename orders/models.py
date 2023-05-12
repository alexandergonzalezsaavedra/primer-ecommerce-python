from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    def __str__(self):
        return f'{self.nombre}'

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria , on_delete=models.CASCADE , null=True)
    precioCompra = models.IntegerField(max_length=30)
    precioVenta = models.IntegerField(max_length=30)
    detalleProducto = models.TextField(max_length=500)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    fechaCreacion = models.DateTimeField()
    fechaModificacion = models.DateTimeField()
    cantidad = models.IntegerField(max_length=30)
    def __str__(self):
        return f'{self.nombre}'