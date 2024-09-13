from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import ProtectedError
from apl.forms import MetodoForm
from apl.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

import re

@method_decorator(never_cache, name='dispatch')
class MetodosListView(ListView):
    model = Metodo_Pago
    template_name = 'Metodos_pago/listar.html'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Metodos de Pagos"
        context['crear_url'] = reverse_lazy('apl:crear_metodo')

        #Para mostrar la alerta de objetos relacionados primero verificamos si existe la variable pk en la url
        #y si lo hay entonces se hace la consulta del metodo de pago para luego mostrar cuales son las realciones que tiene
        #metodo de pago con otros registros

        MetodoPago = Metodo_Pago.objects.get(id = self.request.GET.get('pk')) if self.request.GET.get('pk') else None
        context['obj_relacionados'] = ', '.join([i.__str__() for i in MetodoPago.compras_set.all()] + [i.__str__() for i in MetodoPago.ventas_set.all()]) if MetodoPago else None 
        
        context['entidad'] = "Metodos de pago"
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    
    def get_queryset(self):
        queryset = super().get_queryset()

        # Captura los parámetros de la URL
        id = self.request.GET.get('id')
        nombre = self.request.GET.get('nombre')

        if id:
            if int(id) >= 1:  # Verifica que el número sea positivo
                    queryset = queryset.filter(id=id)
            else:
                messages.error(self.request, "El ID debe ser un número positivo.")

        # Filtra por nombre del cliente
        if nombre:
            if re.match("^[A-Za-z0-9\s]+$", nombre):  # Solo letras, números y espacios
                queryset = queryset.filter(nombre__icontains=nombre)
            else:
                messages.error(self.request, "El nombre no puede contener caracteres especiales")
        return queryset


@method_decorator(never_cache, name='dispatch')
class MetodoCreateView(CreateView):

    model = Metodo_Pago
    form_class = MetodoForm
    template_name = "Metodos_pago/crear.html"
    success_url = reverse_lazy('apl:listar_metodo')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Crear Metodos de Pago"
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
class MetodoUpdateView(UpdateView):

    model = Metodo_Pago
    form_class = MetodoForm
    template_name = "Metodos_pago/crear.html"
    success_url = reverse_lazy('apl:listar_metodo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualizar Metodos de Pago"
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
class MetodoDeleteView(DeleteView):

    model = Metodo_Pago
    template_name = "Metodos_pago/eliminar.html"
    success_url = reverse_lazy('apl:listar_metodo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Eliminar Metodos de Pago"
        context['crear_url'] = reverse_lazy('apl:listar_metodo')
        return context
    
    def post(self, request, *args, **kwargs):

        try:

            response = super().delete(request, args, kwargs)
            messages.success(request, 'Metodo de pago eliminado con exito')
            return response

        except ProtectedError:

            messages.error(request, 'No se ha logrado eliminar la unidad de medida')
            return redirect(self.success_url + f'?pk={self.kwargs.get("pk")}')

        except Exception as e:
            
            messages.error(request, f'Ha ocurrido un error inesperado\n{e}')


    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)