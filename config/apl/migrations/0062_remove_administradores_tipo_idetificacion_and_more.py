# Generated by Django 5.1.1 on 2024-09-29 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apl', '0061_remove_administradores_tipo_documento_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='administradores',
            name='tipo_idetificacion',
        ),
        migrations.AddField(
            model_name='administradores',
            name='tipo_documento',
            field=models.CharField(choices=[('CC', 'Cédula de Ciudadanía'), ('CE', 'Cédula de Extranjería')], default='CC', max_length=3, verbose_name='Tipo de documento'),
        ),
    ]