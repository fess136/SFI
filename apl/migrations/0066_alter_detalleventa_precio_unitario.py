# Generated by Django 5.1.1 on 2024-10-10 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apl', '0065_alter_detalleventa_precio_unitario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleventa',
            name='precio_unitario',
            field=models.DecimalField(decimal_places=2, max_digits=64, null=True, verbose_name='Precio unitario'),
        ),
    ]
