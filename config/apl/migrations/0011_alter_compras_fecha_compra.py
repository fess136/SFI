# Generated by Django 5.0.6 on 2024-06-12 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apl', '0010_alter_compras_fecha_compra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compras',
            name='fecha_compra',
            field=models.DateField(auto_now=True, verbose_name='Fecha De Compra'),
        ),
    ]
