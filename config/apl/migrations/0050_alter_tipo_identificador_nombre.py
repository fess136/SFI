# Generated by Django 5.0.8 on 2024-08-14 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apl', '0049_alter_proveedores_nit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_identificador',
            name='nombre',
            field=models.CharField(max_length=150, unique=True, verbose_name='Nombre'),
        ),
    ]