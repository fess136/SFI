from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apl.forms import PresentacionForm
from django.shortcuts import render
from apl.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


@method_decorator(never_cache, name='dispatch')
class PresentacionListView(ListView):
    model = Presentacion
    template_name = 'Presentaciones/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Presentaciones"
        context['crear_url'] = reverse_lazy('apl:crear_presentacion')
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

@method_decorator(never_cache, name='dispatch')
class PresentacionCreateView(CreateView):

    model = Presentacion
    form_class = PresentacionForm
    template_name = "Presentaciones/crear.html"
    success_url = reverse_lazy('apl:listar_presentacion')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Crear Presentacion"
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

@method_decorator(never_cache, name='dispatch')
class PresentacionUpdateView(UpdateView):

    model = Presentacion
    form_class = PresentacionForm
    template_name = "Presentaciones/crear.html"
    success_url = reverse_lazy('apl:listar_presentacion')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualizar Presentacion"
        return context
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
@method_decorator(never_cache, name='dispatch')
class PresentacionDeleteView(DeleteView):

    model = Presentacion
    template_name = "Presentaciones/eliminar.html"
    success_url = reverse_lazy('apl:listar_presentacion')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Eliminar Presentacion"
        context['crear_url'] = reverse_lazy('apl:listar_presentacion')
        return context
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
