from django.views.generic import ListView
from django.shortcuts import render
from apl.models import *

class ComprasListView(ListView):
    model = C
    template_name = 'Clientes/listar.html'
    