# Generated by Django 4.2.14 on 2024-07-12 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apl', '0019_rename_ventas_unidad_medida_ventas_ventas_unidad_medida'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventas',
            name='ventas_precio',
            field=models.PositiveSmallIntegerField(default=23, verbose_name='Precio'),
            preserve_default=False,
        ),
    ]