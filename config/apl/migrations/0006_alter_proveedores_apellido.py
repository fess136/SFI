# Generated by Django 5.0.6 on 2024-06-12 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apl', '0005_proveedores_apellido_alter_proveedores_nit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedores',
            name='apellido',
            field=models.CharField(default=False, max_length=50, verbose_name='Apellido'),
        ),
    ]
