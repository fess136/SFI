from django.views.generic import ListView
from django.shortcuts import render
from apl.models import *

class IdentificadorListView(ListView):
    model = 
    template_name = 'Tipo_identificador/listar.html'
    
