# Generated by Django 5.0.6 on 2024-06-12 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apl', '0006_alter_proveedores_apellido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedores',
            name='apellido',
            field=models.CharField(max_length=50, verbose_name='Apellido'),
        ),
    ]
