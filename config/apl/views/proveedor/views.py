from django.views.generic import ListView
from django.shortcuts import render
from apl.models import *

class ProveedorListView(ListView):
    model = Proveedores
    template_name = 'Proveedores/listar.html'