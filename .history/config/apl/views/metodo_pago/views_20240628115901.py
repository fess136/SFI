from django.views.generic import ListView
from django.shortcuts import render
from apl.models import *

class MetodosListView(ListView):
    model = Metodo_Pago
    template_name = 'Metodos_pago/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listar Marca'
        context['crear_url'] = reverse_lazy('apl:crear_Marca')
        
        return context