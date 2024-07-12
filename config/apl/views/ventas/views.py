from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy
from apl.forms import VentaForm
from apl.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
#
@method_decorator(never_cache, name='dispatch')
class VentasListView(ListView):
    model = Ventas
    template_name = 'Ventas/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Listar Venta"
        context['crear_url'] = reverse_lazy('apl:crear_venta')
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
@method_decorator(never_cache, name='dispatch')
class VentaCreateView(CreateView):

    model = Ventas
    form_class = VentaForm
    template_name = "Ventas/crear.html"
    success_url = reverse_lazy('apl:listar_venta')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Crear Venta"
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
@method_decorator(never_cache, name='dispatch')
class VentaUpdateView(UpdateView):

    model = Ventas
    form_class = VentaForm
    template_name = "Ventas/crear.html"
    success_url = reverse_lazy('apl:listar_venta')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualizar Venta"
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
@method_decorator(never_cache, name='dispatch')
class VentaDeleteView(DeleteView):

    model = Ventas
    template_name = "Ventas/eliminar.html"
    success_url = reverse_lazy('apl:listar_venta')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Eliminar Venta"
        context['crear_url'] = reverse_lazy('apl:listar_venta')
        return context
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)