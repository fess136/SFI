from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import ProtectedError
from apl.forms import IdentificadorForm
from apl.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

import re

@method_decorator(never_cache, name='dispatch')
class IdentificadorListView(ListView):
    model = Tipo_identificador
    template_name = 'Tipo_identificador/listar.html'

    #decorador para proteccion de la vista desde el login

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Tipos de Identificadores"
        context['crear_url'] = reverse_lazy('apl:crear_identificador')
        context['entidad'] = "Tipo de identificador"
        context['obj_relacionados'] = [i.__str__() for i in Tipo_identificador.objects.get(id = self.request.GET.get('pk')).clientes_set.all()] if self.request.GET.get('pk') else None
        
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        # Obtiene los parámetros de consulta de la URL
        id = self.request.GET.get('id')
        nombre = self.request.GET.get('nombre')
        estado = self.request.GET.get('estado')

        # Filtra los resultados según los parámetros proporcionados
        if id:
            if int(id) >= 1:  # Verifica que el número sea positivo
                    queryset = queryset.filter(id=id)
            else:
                messages.error(self.request, "El ID debe ser un número válido.")
                
        if nombre:
            if re.match("^[A-Za-z0-9\s]+$", nombre):  # Solo letras, números y espacios
                queryset = queryset.filter(nombre__icontains=nombre)
            else:
                messages.error(self.request, "El nombre no puede contener caracteres especiales.")
                
        if estado:
                queryset = queryset.filter(estado__iexact=estado)  # Filtra por estado
                
        return queryset


@method_decorator(never_cache, name='dispatch')
class IdentificadorCreateView(CreateView):

    model = Tipo_identificador
    form_class = IdentificadorForm
    template_name = "Tipo_identificador/crear.html"
    success_url = reverse_lazy('apl:listar_identificador')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Crear Tipo de Identificador"
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
        
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
@method_decorator(never_cache, name='dispatch')
class IdentificadorUpdateView(UpdateView):

    model = Tipo_identificador
    form_class = IdentificadorForm
    template_name = "Tipo_identificador/crear.html"
    success_url = reverse_lazy('apl:listar_identificador')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualizar Tipo de Identificador"
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
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
@method_decorator(never_cache, name='dispatch')
class IdentificadorDeleteView(DeleteView):

    model = Tipo_identificador
    template_name = "Tipo_identificador/eliminar.html"
    success_url = reverse_lazy('apl:listar_identificador')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Eliminar Tipo de Identificador"
        context['crear_url'] = reverse_lazy('apl:listar_identificador')
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        
        try:

            response = super().delete(request, args, kwargs)
            messages.success(request, "Tipo de identificador eliminado con éxito.")
            return response
            
        except ProtectedError:

            messages.error(request, f"No se ha logrado eliminar el Tipo de identificador.")
            return redirect(self.success_url + f"?pk={self.kwargs.get('pk')}")
        
        except Exception as e:

            messages.error(request, f"Ha ocurrido un error inesperado \n{e}")