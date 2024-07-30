from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from apl.forms import CompraForm
from apl.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


@method_decorator(never_cache, name='dispatch')
class ComprasListView(ListView):
    model = Compras
    template_name = 'Compras/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Compras"
        context['crear_url'] = reverse_lazy('apl:crear_compra')
        context['entidad'] = "Compras"
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)



@method_decorator(never_cache, name='dispatch')
class CompraCreateView(CreateView):

    model = Compras
    form_class = CompraForm
    template_name = "Compras/crear.html"
    success_url = reverse_lazy('apl:crear_detallecompra')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Crear Compra"
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
@method_decorator(never_cache, name='dispatch')
class CompraUpdateView(UpdateView):

    model = Compras
    form_class = CompraForm
    template_name = "Compras/crear.html"
    success_url = reverse_lazy('apl:listar_compra')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualizar Compra"
        return context
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
@method_decorator(never_cache, name='dispatch')
class CompraDeleteView(DeleteView):

    model = Compras
    template_name = "Compras/eliminar.html"
    success_url = reverse_lazy('apl:listar_compra')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Eliminar Compra"
        context['crear_url'] = reverse_lazy('apl:listar_compra')
        return context
    
      #decorador para proteccion de la vista desde el login
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

    
