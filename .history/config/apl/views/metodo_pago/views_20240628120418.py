from typing import Any
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from apl.forms import MetodoPagoForm
from apl.models import *

class MetodosListView(ListView):
    model = Metodo_Pago
    template_name = 'Metodos_pago/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listar metodo'
        context['crear_url'] = reverse_lazy('apl:crear_Metodo')
        
        return context
    
class MetodoCreateView(CreateView):
    model = Metodo_Pago
    form_class = MetodoPagoForm
    template_name = 'Metodos_pago/crear.html'
    success_url = reverse_lazy('apl:listar_metodo')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Metodo'
        
        return context

class MetodoupdateView(UpdateView):
    