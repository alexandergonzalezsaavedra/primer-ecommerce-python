# Generated by Django 4.2.1 on 2023-05-31 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_rename_name_categoria_nombre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='imagenCategoria',
            field=models.ImageField(blank=True, null=True, upload_to='productos/'),
        ),
    ]
