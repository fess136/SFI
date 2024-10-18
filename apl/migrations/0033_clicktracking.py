# Generated by Django 5.0.7 on 2024-07-31 15:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apl', '0032_remove_ventas_administrador_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClickTracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('detalle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apl.detallecompra')),
            ],
        ),
    ]