# Generated by Django 4.2.14 on 2024-07-12 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apl', '0021_remove_ventas_ventas_precio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ventas',
            name='ventas_unidad_medida',
        ),
    ]
