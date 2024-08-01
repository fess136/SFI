# Generated by Django 5.0.7 on 2024-07-31 20:16

import apl.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apl', '0035_detallecompra_finalizado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[apl.models.validacion_numeros_negativos], verbose_name='Precio'),
        ),
    ]
