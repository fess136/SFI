# Generated by Django 5.0.7 on 2024-07-29 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apl', '0028_merge_20240727_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallecompra',
            name='cantidad',
            field=models.PositiveIntegerField(null=True, verbose_name='Cantidad'),
        ),
    ]
