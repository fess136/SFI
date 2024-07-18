# Generated by Django 5.0.6 on 2024-07-10 20:17

import apl.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apl', '0016_alter_proveedores_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administradores',
            name='correo_electronico',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='nit',
            field=models.PositiveBigIntegerField(unique=True, verbose_name='Numero de Identificacion'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='telefono',
            field=models.PositiveIntegerField(validators=[apl.models.validacion_telefono], verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='compras',
            name='fecha_compra',
            field=models.DateField(auto_now=True, verbose_name='Fecha De Compra'),
        ),
    ]
