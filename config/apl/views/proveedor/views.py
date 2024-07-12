from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from apl.forms import ProveedorForm
from apl.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


@method_decorator(never_cache, name='dispatch')
class ProveedorListView(ListView):
    model = Proveedores
    template_name = 'Proveedores/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Listar Proveedores"
        context['crear_url'] = reverse_lazy('apl:crear_proveedor')
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

@method_decorator(never_cache, name='dispatch')
class ProveedorCreateView(CreateView):

    model = Proveedores
    form_class = ProveedorForm
    template_name = "Proveedores/crear.html"
    success_url = reverse_lazy('apl:listar_proveedor')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Crear Proveedor"
        return context
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
@method_decorator(never_cache, name='dispatch')
class ProveedorUpdateView(UpdateView):

    model = Proveedores
    form_class = ProveedorForm
    template_name = "Proveedores/crear.html"
    success_url = reverse_lazy('apl:listar_proveedor')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualizar Proveedor"
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

@method_decorator(never_cache, name='dispatch')
class ProveedorDeleteView(DeleteView):

    model = Proveedores
    template_name = "Proveedores/eliminar.html"
    success_url = reverse_lazy('apl:listar_proveedor')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Eliminar Proveedor"
        context['crear_url'] = reverse_lazy('apl:listar_proveedor')
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)