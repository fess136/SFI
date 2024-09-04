from django.http import JsonResponse
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.exceptions import ValidationError
from apl.models import Administradores
from apl.forms import AdministradorForm
from django.views.decorators.cache import never_cache
@method_decorator(never_cache , name='dispatch')
@method_decorator(login_required, name='dispatch')
class AdministradorListView(ListView):
    model = Administradores
    template_name = 'administrador/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Administradores'
        context['entidad'] = 'Administradores'
        context['crear_url'] = reverse_lazy('apl:crear_administrador')
        context['entidad'] = "Administradores"
        return context
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    

@method_decorator(never_cache , name='dispatch')
@method_decorator(login_required, name='dispatch')
class AdministradorCreateView(CreateView):
    model = Administradores
    form_class = AdministradorForm
    template_name = 'administrador/crear.html'
    success_url = reverse_lazy('apl:listar_administrador')
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Administrador'
        context['entidad'] = 'Registrar administrador'
        context['listar_url'] = reverse_lazy('apl:listar_administrador')
        context['crear_url'] = reverse_lazy('apl:listar_administrador')
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

@method_decorator(never_cache , name='dispatch')
@method_decorator(login_required, name='dispatch')
class AdministradorUpdateView(UpdateView):
    model = Administradores
    form_class = AdministradorForm
    template_name = 'administrador/crear.html'
    success_url = reverse_lazy('apl:listar_administrador')
    

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar administrador'
        context['entidad'] = 'Editar administrador'
        context['listar_url'] = reverse_lazy('apl:listar_administrador')
        context['crear_url'] = reverse_lazy('apl:listar_administrador')
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
@method_decorator(never_cache , name='dispatch')
@method_decorator(login_required, name='dispatch')
class AdministradorDeleteView(DeleteView):
    model = Administradores
    template_name = 'administrador/eliminar.html'
    success_url = reverse_lazy('apl:listar_administrador')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar administrador'
        context['entidad'] = 'Eliminar administrador'
        context['listar_url'] = reverse_lazy('apl:listar_administrador')
        return context
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        
        try:

            response = super().delete(request, args, kwargs)
            messages.success(request, "Administrador eliminado con éxito.")
            return response
            
        except Exception as e:

            messages.error(request, f"No se ha logrado eliminado el Administrador\n{e}")
            return redirect(self.success_url)