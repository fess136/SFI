from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render
from apl.forms import EmpleadoForm
from apl.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

@method_decorator(never_cache, name='dispatch')
class EmpleadoListView(ListView):
    model = Empleados
    template_name = 'Empleados/listar.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Listar Empleados"
        context['crear_url'] = reverse_lazy('apl:crear_empleado')
        return context
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

@method_decorator(never_cache, name='dispatch')
class EmpleadoCreateView(CreateView):

    model = Empleados
    form_class = EmpleadoForm
    template_name = "Empleados/crear.html"
    success_url = reverse_lazy('apl:listar_empleado')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Crear Empleados"
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)    

@method_decorator(never_cache, name='dispatch')
class EmpleadoUpdateView(UpdateView):

    model = Empleados
    form_class = EmpleadoForm
    template_name = "Empleados/crear.html"
    success_url = reverse_lazy('apl:listar_empleado')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualizar Empleados"
        return context
        
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

@method_decorator(never_cache, name='dispatch')
class EmpleadoDeleteView(DeleteView):

    model = Empleados
    template_name = "Empleados/eliminar.html"
    success_url = reverse_lazy('apl:listar_empleado')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Eliminar Empleados"
        context['crear_url'] = reverse_lazy('apl:listar_empleado')
        return context
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
