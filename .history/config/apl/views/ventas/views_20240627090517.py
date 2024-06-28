from django.views.generic import ListView
from django.shortcuts import render
from apl.models import *

class VentasListView(ListView):
    model = Ventas
    template_name = 'Ventas/listar.html'
    
