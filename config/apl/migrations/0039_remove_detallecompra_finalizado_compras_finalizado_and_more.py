# Generated by Django 5.1 on 2024-08-21 19:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apl', '0038_remove_ventas_producto_remove_ventas_ventas_cantidad_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallecompra',
            name='finalizado',
        ),
        migrations.AddField(
            model_name='compras',
            name='finalizado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ventas',
            name='finalizado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ventas',
            name='metodo_pago',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='apl.metodo_pago'),
        ),
    ]