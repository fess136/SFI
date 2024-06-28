from typing import Any
from django.views.generic import ListView,CreateView, UpdateView, DeleteView
from django.shortcuts import render
from apl.models import *
from django.urls import reverse_lazy
from apl.forms import CompraForm

class CompraListView(ListView):
    model = Compras
    template_name = 'Compras/listar.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['titulo'] = 'Listar Compra'
        context ['crear_url'] = reverse_lazy('apl:crear_compra')
        
        return context
    
class CompraCreateView(CreateView):
    
    model = Compras
    form_class = CompraForm
    template_name = 'Compras/crear.html'
    success_url = reverse_lazy('apl:listar_compra')
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Compra'
        
        return context
    
class CompraUpdateView(UpdateView):
    
    model = Compras
    form_class = CompraForm
    template_name = 'Compras/crear.html'
    success_url = reverse_lazy('apl:listar_compra')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Compra'
        
        return context
    
class CompraDeleteView(UpdateView):
    
    model = Compras
    template_name = 'Compras/eliminar.html'
    success_url = reverse_lazy('apl:listar_compra')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['titulo'] = 'Actualizar Compra'
        context ['crear_url'] =