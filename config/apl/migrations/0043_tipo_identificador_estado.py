# Generated by Django 4.2.15 on 2024-09-02 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apl', '0042_alter_administradores_numero_documento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipo_identificador',
            name='estado',
            field=models.CharField(choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default='activo', max_length=10, verbose_name='Estado'),
        ),
    ]
