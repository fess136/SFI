from django.contrib import admin
from apl.models import*
# Register your models here.
admin.site.register(Tipo)

admin.site.register(Tipo_identificador,Empleados,Clientes)