# Generated by Django 5.0.8 on 2024-08-14 14:25

import apl.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apl', '0048_alter_proveedores_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedores',
            name='nit',
            field=models.CharField(max_length=20, unique=True, validators=[apl.models.validacion_telefono], verbose_name='Nit/Cedula'),
        ),
    ]
