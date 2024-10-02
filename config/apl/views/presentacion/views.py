from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apl.forms import PresentacionForm
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import ProtectedError
from apl.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

import re

@method_decorator(never_cache, name='dispatch')
class PresentacionListView(ListView):
    model = Presentacion
    template_name = 'Presentaciones/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Presentaciones"
        context['crear_url'] = reverse_lazy('apl:crear_presentacion')
        context['obj_relacionados'] = ', '.join([i.__str__() for i in Presentacion.objects.get(id = self.request.GET.get('pk')).productos_set.all()]) if self.request.GET.get('pk') else None
        context['entidad'] = "Presentaciones"
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = super().get_queryset()

        # Captura los parámetros de la URL
        id = self.request.GET.get('id')
        descripcion = self.request.GET.get('descripcion')

        if id:
            if int(id) >= 1:  # Verifica que el número sea positivo
                    queryset = queryset.filter(id=id)
            else:
                messages.error(self.request, "El ID debe ser un número positivo.")

        # Filtra por nombre del cliente
        if descripcion:
            if re.match("^[A-Za-z0-9\s]+$", descripcion):  # Solo letras, números y espacios
                queryset = queryset.filter(descripcion__icontains=descripcion)
            else:
                messages.error(self.request, "El nombre no puede contener caracteres especiales")
        return queryset

@method_decorator(never_cache, name='dispatch')
class PresentacionCreateView(CreateView):

    model = Presentacion
    form_class = PresentacionForm
    template_name = "Presentaciones/crear.html"
    success_url = reverse_lazy('apl:listar_presentacion')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Crear Presentacion"
        context['crear_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        presentacion = form.save()
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'status': 'success',
                                 'nombre': presentacion.__str__(),
                                 'id': presentacion.id
                                 })
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
class PresentacionUpdateView(UpdateView):

    model = Presentacion
    form_class = PresentacionForm
    template_name = "Presentaciones/crear.html"
    success_url = reverse_lazy('apl:listar_presentacion')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualizar Presentacion"
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

    def post(self, request, *args, **kwargs):
        
        try:

            response = super().delete(request, args, kwargs)
            messages.success(request, "Presentación eliminada con éxito.")
            return response
            
        except ProtectedError:

            messages.error(request, f"No se ha logrado eliminar la Presentación.")
            return redirect(self.success_url + f"?pk={self.kwargs.get('pk')}")
        
        except Exception as e:

            messages.error(request, f"Ha ocurrido un error inesperado \n{e}")