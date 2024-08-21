from django.http import JsonResponse
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
        context['titulo'] = "Empleados"
        context['crear_url'] = reverse_lazy('apl:crear_empleado')
        context['entidad'] = "Empleados"
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
        context['crear_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'status': 'success'})
        return response

    def form_invalid(self, form):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            errors = {}
            for field, error_list in form.errors.items():
                errors[field] = [str(error) for error in error_list]
            return JsonResponse({
                'status': 'error',
                'errors': errors
            }, status=400)
    
        return super().form_invalid(form)
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
        context['crear_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'status': 'success'})
        return response

    def form_invalid(self, form):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            errors = {}
            for field, error_list in form.errors.items():
                errors[field] = [str(error) for error in error_list]
            return JsonResponse({
                'status': 'error',
                'errors': errors
            }, status=400)
        return super().form_invalid(form)

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
