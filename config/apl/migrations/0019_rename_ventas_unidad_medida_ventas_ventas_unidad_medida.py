# Generated by Django 4.2.14 on 2024-07-11 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apl', '0018_ventas_ventas_cantidad_ventas_ventas_unidad_medida'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ventas',
            old_name='ventas_unidad_Medida',
            new_name='ventas_unidad_medida',
        ),
    ]
