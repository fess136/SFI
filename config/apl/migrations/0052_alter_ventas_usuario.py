# Generated by Django 5.1.1 on 2024-09-12 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apl', '0051_alter_proveedores_nit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventas',
            name='usuario',
            field=models.CharField(max_length=100, verbose_name='Usuario'),
        ),
    ]
