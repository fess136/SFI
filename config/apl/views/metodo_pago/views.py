from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from apl.forms import MetodoForm
from apl.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


@method_decorator(never_cache, name='dispatch')
class MetodosListView(ListView):
    model = Metodo_Pago
    template_name = 'Metodos_pago/listar.html'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Metodos de Pagos"
        context['crear_url'] = reverse_lazy('apl:crear_metodo')
        context['entidad'] = "Metodos de pago"
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)


@method_decorator(never_cache, name='dispatch')
class MetodoCreateView(CreateView):

    model = Metodo_Pago
    form_class = MetodoForm
    template_name = "Metodos_pago/crear.html"
    success_url = reverse_lazy('apl:listar_metodo')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Crear Metodos de Pago"
        return context
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
@method_decorator(never_cache, name='dispatch')
class MetodoUpdateView(UpdateView):

    model = Metodo_Pago
    form_class = MetodoForm
    template_name = "Metodos_pago/crear.html"
    success_url = reverse_lazy('apl:listar_metodo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualizar Metodos de Pago"
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
@method_decorator(never_cache, name='dispatch')
class MetodoDeleteView(DeleteView):

    model = Metodo_Pago
    template_name = "Metodos_pago/eliminar.html"
    success_url = reverse_lazy('apl:listar_metodo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Eliminar Metodos de Pago"
        context['crear_url'] = reverse_lazy('apl:listar_metodo')
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)