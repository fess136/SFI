from django.views.generic import ListView
from django.shortcuts import render
from apl.models import *

class VentasListView(ListView):
    model = v
    template_name = 'Presentaciones/listar.html'
    
