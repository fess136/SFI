# Generated by Django 5.1 on 2024-08-21 18:32

import apl.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apl', '0036_alter_productos_precio'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(validators=[apl.models.validacion_numeros_negativos], verbose_name='Cantidad')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apl.productos')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apl.ventas')),
            ],
        ),
    ]
