from django.views.generic import ListView ,CreateView, UpdateView, DeleteView
from django.shortcuts import render
from apl.models import *
from django.urls import reverse_lazy
from apl.forms import Presentacionform

class PresentacionListView(ListView):
    model = Presentacion
    template_name = 'Presentaciones/listar.html'
    
def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listar Presentacion'
        context['crear_url'] = reverse_lazy('apl:crear_presentacion')
        
        return context

class PresentacionCreateView(CreateView):
    
    model = Clientes
    form_class = Presentacionform
    template_name = 'Presentacion/crear.html'
    success_url = reverse_lazy('apl:listar_cliente')
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Cliente'
        
        return context

class PresentacionUpdateView(UpdateView):
    model = Clientes
    form_class = Presentacionform
    template_name = 'Presentacion/crear.html'
    success_url = reverse_lazy('apl:listar_cliente')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context  ['titulo'] = 'Actualizar Cliente'
        
        return context
    
class PresentacionDeleteView(DeleteView):
    model = Clientes
    template_name = 'Presentacion/eliminar.html'
    success_url = reverse_lazy('apl:listar_cliente')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context  ['titulo'] = 'Actualizar Cliente'
        context['crear_url'] = reverse_lazy('apl:listar_cliente')
        
        return context