# Generated by Django 5.1.1 on 2024-09-29 20:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apl', '0058_alter_administradores_tipo_documento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administradores',
            name='tipo_documento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='apl.tipo_identificador', verbose_name='Tipo de documento'),
        ),
    ]