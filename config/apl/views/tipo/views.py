from django.views.generic import ListView
from django.shortcuts import render
from apl.models import *

class TipoListView(ListView):
    model = Tipo
    template_name = 'tipo/listar.html'
    

