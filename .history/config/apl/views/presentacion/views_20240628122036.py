from django.views.generic import ListView
from django.shortcuts import render
from apl.models import *

class PresentacionListView(ListView):
    model = Presentacion
    template_name = 'Presentaciones/listar.html'
    
def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listar Clientes'
        context['crear_url'] = reverse_lazy('apl:crear_cliente')
        
        return context

class ClienteCreateView(CreateView):
    
    model = Clientes
    form_class = Clienteform
    template_name = 'Clientes/crear.html'
    success_url = reverse_lazy('apl:listar_cliente')
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Cliente'
        
        return context

class ClienteUpdateView(UpdateView):
    model = Clientes
    form_class = Clienteform
    template_name = 'Clientes/crear.html'
    success_url = reverse_lazy('apl:listar_cliente')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context  ['titulo'] = 'Actualizar Cliente'
        
        return context
    
class ClienteDeleteView(DeleteView):
    model = Clientes
    template_name = 'Clientes/eliminar.html'
    success_url = reverse_lazy('apl:listar_cliente')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context  ['titulo'] = 'Actualizar Cliente'
        context['crear_url'] = reverse_lazy('apl:listar_cliente')
        
        return context