from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render
from apl.forms import EmpleadoForm
from apl.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class EmpleadoListView(ListView):
    model = Empleados
    template_name = 'Empleados/listar.html'
<<<<<<< HEAD
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Listar Empleados"
        context['crear_url'] = reverse_lazy('apl:crear_empleado')
        return context



class EmpleadoCreateView(CreateView):

    model = Empleados
    form_class = EmpleadoForm
    template_name = "Empleados/crear.html"
    success_url = reverse_lazy('apl:listar_empleado')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Crear Empleados"
        return context
    
class EmpleadoUpdateView(UpdateView):

    model = Empleados
    form_class = EmpleadoForm
    template_name = "Empleados/crear.html"
    success_url = reverse_lazy('apl:listar_empleado')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualizar Empleados"
        return context
    
class EmpleadoDeleteView(DeleteView):

    model = Empleados
    template_name = "Empleados/eliminar.html"
    success_url = reverse_lazy('apl:listar_empleado')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Eliminar Empleados"
        context['crear_url'] = reverse_lazy('apl:listar_empleado')
        return context
=======
      #decorador para proteccion de la vista desde el login
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

>>>>>>> main
