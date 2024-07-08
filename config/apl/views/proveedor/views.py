from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from apl.forms import ProveedorForm
from apl.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class ProveedorListView(ListView):
    model = Proveedores
    template_name = 'Proveedores/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Listar Proveedores"
        context['crear_url'] = reverse_lazy('apl:crear_proveedor')
        return context



class ProveedorCreateView(CreateView):

    model = Proveedores
    form_class = ProveedorForm
    template_name = "Proveedores/crear.html"
    success_url = reverse_lazy('apl:listar_proveedor')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Crear Proveedor"
        return context
    
class ProveedorUpdateView(UpdateView):

    model = Proveedores
    form_class = ProveedorForm
    template_name = "Proveedores/crear.html"
    success_url = reverse_lazy('apl:listar_proveedor')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualizar Proveedor"
        return context
    
class ProveedorDeleteView(DeleteView):

    model = Proveedores
    template_name = "Proveedores/eliminar.html"
    success_url = reverse_lazy('apl:listar_proveedor')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Eliminar Proveedor"
        context['crear_url'] = reverse_lazy('apl:listar_proveedor')
        return context
