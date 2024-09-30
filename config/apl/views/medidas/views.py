from django.http import JsonResponse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import ProtectedError
from apl.forms import MedidaForm
from apl.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

import re

@method_decorator(never_cache, name='dispatch')
class MedidasListView(ListView):
    model = Unidad_Medida
    template_name = 'Unidades_medida/listar.html'

      #decorador para proteccion de la vista desde el login

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Unidades de Medida"
        context['crear_url'] = reverse_lazy('apl:crear_medida')
        context['entidad'] = "Medidas"
        context['obj_relacionados'] = [i.__str__() for i in Unidad_Medida.objects.get(id = self.request.GET.get('pk')).productos_set.all()] if self.request.GET.get('pk') else None
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
                queryset = queryset.filter(descripcion__icontains=nombre)
            else:
                messages.error(self.request, "El nombre no puede contener caracteres especiales.")
                
        if estado:
                queryset = queryset.filter(estado__iexact=estado)  # Filtra por estado
                
        return queryset

@method_decorator(never_cache, name='dispatch')
class MedidaCreateView(CreateView):

    model = Unidad_Medida
    form_class = MedidaForm
    template_name = "Unidades_medida/crear.html"
    success_url = reverse_lazy('apl:listar_medida')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Crear Unidad de Medida"
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
class MedidaUpdateView(UpdateView):

    model = Unidad_Medida
    form_class = MedidaForm
    template_name = "Unidades_medida/crear.html"
    success_url = reverse_lazy('apl:listar_medida')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualizar Unidad de Medida"
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
class MedidaDeleteView(DeleteView):

    model = Unidad_Medida
    template_name = "Unidades_medida/eliminar.html"
    success_url = reverse_lazy('apl:listar_medida')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Eliminar Unidad de Medida"
        context['crear_url'] = reverse_lazy('apl:listar_medida')
        return context
    
    def post(self, request, *args, **kwargs):
        
        try:

            response = super().delete(request, args, kwargs)
            messages.success(request, "Unidad de medida eliminada con éxito.")
            return response
            
        except ProtectedError:

            messages.error(request, f"No se ha logrado eliminar la unidad de medida.")
            return redirect(self.success_url + f"?pk={self.kwargs.get('pk')}")
        
        except Exception as e:

            messages.error(request, f"Ha ocurrido un error inesperado \n{e}")
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)