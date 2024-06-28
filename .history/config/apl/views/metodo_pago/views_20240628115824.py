from django.views.generic import ListView
from django.shortcuts import render
from apl.models import *

class MetodosListView(ListView):
    model = Metodo_Pago
    template_name = 'Metodos_pago/listar.html'
