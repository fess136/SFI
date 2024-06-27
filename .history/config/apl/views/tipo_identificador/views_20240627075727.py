from django.views.generic import ListView
from django.shortcuts import render
from apl.models import *

class IdentificadoresListView(ListView):
    model = Presentacion
    template_name = 'Presentaciones/listar.html'
    
