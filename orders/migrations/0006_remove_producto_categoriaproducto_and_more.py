# Generated by Django 4.2.1 on 2023-06-07 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_categoria_imagencategoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='categoriaProducto',
        ),
        migrations.AddField(
            model_name='producto',
            name='categoriaProducto',
            field=models.ManyToManyField(to='orders.categoria'),
        ),
    ]
