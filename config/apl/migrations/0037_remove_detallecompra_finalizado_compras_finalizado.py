# Generated by Django 5.0.8 on 2024-08-06 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apl', '0036_alter_productos_precio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallecompra',
            name='finalizado',
        ),
        migrations.AddField(
            model_name='compras',
            name='finalizado',
            field=models.BooleanField(default=False, null=True),
        ),
    ]