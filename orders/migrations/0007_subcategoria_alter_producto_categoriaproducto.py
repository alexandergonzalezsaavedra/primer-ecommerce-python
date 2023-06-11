# Generated by Django 4.2.1 on 2023-06-09 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_remove_producto_categoriaproducto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subcategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreSubcategoria', models.CharField(max_length=100)),
                ('imagenSubcategoria', models.ImageField(blank=True, null=True, upload_to='productos/')),
                ('descripcionSubcategoria', models.TextField(max_length=500, null=True)),
                ('subcategoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.categoria')),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoriaProducto',
            field=models.ManyToManyField(to='orders.subcategoria'),
        ),
    ]
