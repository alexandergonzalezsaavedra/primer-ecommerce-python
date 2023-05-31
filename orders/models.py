from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    imagenCategoria = models.ImageField(upload_to='productos/', blank=True, null=True)
    descripcion = models.TextField(max_length=500 , null=True)
    def __str__(self):
        return f'{self.nombre}'

class Producto(models.Model):
    nombreProducto = models.CharField(max_length=100, null=True)
    categoriaProducto = models.ForeignKey(Categoria , on_delete=models.CASCADE , null=True)
    precioCompraProducto = models.IntegerField(null=True)
    precioVentaProducto = models.IntegerField(null=True)
    detalleProducto = models.TextField(max_length=500, null=True)
    imagenProducto = models.ImageField(upload_to='productos/', blank=True, null=True)
    fechaCreacionProducto = models.DateTimeField(null=True)
    fechaModificacionProducto = models.DateTimeField(null=True)
    existenciaProducto = models.IntegerField(null=True)
    def __str__(self):
        return f'{self.nombreProducto}'

class Historial(models.Model):
    productoHistorial = models.ForeignKey(Producto , on_delete=models.CASCADE , null=True)
    def __str__(self):
        return f'{self.productoHistorial}'

class OrdenCompra(models.Model):
    productoOrdenCompra = models.ForeignKey(Producto , on_delete=models.CASCADE , null=True)
    fechaCreacionOrdenCompra = models.DateTimeField(null=True)
    estadoOrdenCompra = models.BooleanField(null=True)
    def __str__(self):
        return f'{self.productoOrdenCompra}'