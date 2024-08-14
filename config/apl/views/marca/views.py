from typing import Any
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apl.forms import MarcaForm
from apl.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


@method_decorator(never_cache, name='dispatch')
class MarcaListView(ListView):
    model = Marcas
    template_name = 'marca/listar.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Marcas"
        context['crear_url'] = reverse_lazy('apl:crear_marca')
        context['entidad'] = "Marcas"
        return context

@method_decorator(never_cache, name='dispatch')
class MarcaCreateView(CreateView):

    model = Marcas
    form_class = MarcaForm
    template_name = "Marca/crear.html"
    success_url = reverse_lazy('apl:listar_marca')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo'] = "Crear Marca"
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
    

@method_decorator(never_cache, name='dispatch')
class MarcaUpdateView(UpdateView):

    model = Marcas
    form_class = MarcaForm
    template_name = 'Marca/crear.html'
    success_url = reverse_lazy('apl:listar_marca')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualizar Marca"
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
    
@method_decorator(never_cache, name='dispatch')
class MarcaDeleteView(DeleteView):

    model = Marcas
    template_name = "Marca/eliminar.html"
    success_url = reverse_lazy('apl:listar_marca')
    
    #decorador para proteccion de la vista desde el login
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Marca'
        context["crear_url"] = reverse_lazy("apl:listar_marca")
        return context