# Generated by Django 4.2.14 on 2024-07-12 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apl', '0020_ventas_ventas_precio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ventas',
            name='ventas_precio',
        ),
    ]