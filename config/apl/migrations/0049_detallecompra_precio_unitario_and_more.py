# Generated by Django 5.1.1 on 2024-09-09 19:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apl', '0048_alter_clientes_correo_electronico_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallecompra',
            name='precio_unitario',
            field=models.PositiveIntegerField(null=True, verbose_name='Precio unitario'),
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='precio_unitario',
            field=models.PositiveIntegerField(null=True, verbose_name='Precio unitario'),
        ),
        migrations.AlterField(
            model_name='compras',
            name='usuario',
            field=models.CharField(max_length=100, verbose_name='Usuario'),
        ),
        migrations.AlterField(
            model_name='detalleventa',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='apl.productos'),
        ),
        migrations.AlterField(
            model_name='detalleventa',
            name='venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='apl.ventas'),
        ),
        migrations.AlterField(
            model_name='ventas',
            name='usuario',
            field=models.CharField(max_length=100, verbose_name='Usuario'),
        ),
    ]
