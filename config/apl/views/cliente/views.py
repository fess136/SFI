from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from apl.forms import ClienteForm
from apl.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


@method_decorator(never_cache, name='dispatch')
class ClienteListView(ListView):
    model = Clientes
    template_name = 'Clientes/listar.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Clientes"
        context['crear_url'] = reverse_lazy('apl:crear_cliente')
        context['entidad'] = "Clientes"
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

@method_decorator(never_cache, name='dispatch')
class ClienteCreateView(CreateView):

    model = Clientes
    form_class = ClienteForm
    template_name = "Clientes/crear.html"
    success_url = reverse_lazy('apl:listar_cliente')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Crear Cliente"
        return context
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
@method_decorator(never_cache, name='dispatch')
class ClienteUpdateView(UpdateView):

    model = Clientes
    form_class = ClienteForm
    template_name = "Clientes/crear.html"
    success_url = reverse_lazy('apl:listar_cliente')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualizar Cliente"
        return context
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
@method_decorator(never_cache, name='dispatch')
class ClienteDeleteView(DeleteView):

    model = Clientes
    template_name = "Clientes/eliminar.html"
    success_url = reverse_lazy('apl:listar_cliente')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Eliminar Cliente"
        context['crear_url'] = reverse_lazy('apl:listar_cliente')
        return context
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
