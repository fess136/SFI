# Generated by Django 5.0.6 on 2024-06-12 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apl', '0004_unidad_medida_estado_alter_clientes_telefono_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedores',
            name='apellido',
            field=models.CharField(default=True, max_length=50, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='nit',
            field=models.CharField(max_length=20, unique=True, verbose_name='Nit/Cedula'),
        ),
    ]