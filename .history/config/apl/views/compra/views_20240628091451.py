from typing import Any
from django.views.generic import ListView
from django.shortcuts import render
from apl.models import *

class ComprasListView(ListView):
    model = Compras
    template_name = 'Compras/listar.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['titulo'] = 'Listar Compra'
    