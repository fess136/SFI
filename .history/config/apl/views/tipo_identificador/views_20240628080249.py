from typing import Any
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from apl.forms import TipoIdentificadorForm
from apl.models import *

class IdentificadorListView(ListView):
    model = Tipo_identificador
    template_name = 'Tipo_identificador/listar.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listar Tipo De Identificador'
        context['crear_url'] = reverse_lazy('apl:crear_identificador')
        
        return context
    
class IdentificadorCreateView(CreateView):
    
    model = Tipo_identificador
    form_class = TipoIdentificadorForm
    template_name = 'Tipo_identificador/crear.html'
    success_url = reverse_lazy('apl:listar_identificador')
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Tipo De Identificador'
        
        return context
    
class IdentificadorUpdateView(UpdateView):
    
    model = Tipo_identificador
    form_class = TipoIdentificadorForm
    template_name = 'Tipo_identificador/crear.html'
    success_url = reverse_lazy('apl:listar_identificador')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Identificador'
        
        return context
    
class IdentificadorDeleteView(DeleteView):
    
    model = Tipo_identificador
    