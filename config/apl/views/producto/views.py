from django.views.generic import ListView
from django.shortcuts import render
from apl.models import *

class ProductoListView(ListView):
    model = Productos
    template_name = 'Productos/listar.html'