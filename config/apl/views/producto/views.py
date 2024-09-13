from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apl.forms import ProductosForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import ProtectedError, Q
from apl.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

import logging
import re


@method_decorator(never_cache, name='dispatch')
class ProductoListView(ListView):
    model = Productos
    template_name = 'Productos/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Productos"
        context['crear_url'] = reverse_lazy('apl:crear_producto')
        Producto = Productos.objects.get(id = self.request.GET.get('pk')) if self.request.GET.get('pk') else None
        context['obj_relacionados'] = ', '.join([i.__str__() for i in Producto.detallecompra_set.all()] + [i.__str__() for i in Producto.detalleventa_set.all()]) if Producto else None
        context['entidad'] = "Productos"
        return context
    
    
    logger = logging.getLogger(__name__)
    def get_queryset(self):
        queryset = super().get_queryset()

        # Captura los parámetros de la URL
        id = self.request.GET.get('id')
        nombre = self.request.GET.get('nombre')
        marcas = self.request.GET.get('marcas')
        tipo = self.request.GET.get('tipo')
        presentacion = self.request.GET.get('presentacion')
        unidad_medida = self.request.GET.get('unidad_medida')

        if id:
            if int(id) >= 1:  # Verifica que el número sea positivo
                    queryset = queryset.filter(id=id)
            else:
                messages.error(self.request, "El ID debe ser un número positivo.")

        # Filtra por nombre del producto
        if nombre:
            if re.match("^[A-Za-z0-9\s]+$", nombre):  # Solo letras, números y espacios
                queryset = queryset.filter(nombre__icontains=nombre)
            else:
                messages.error(self.request, "El nombre no puede contener caracteres especiales")

        # Filtra por nombre de la marca (relación ForeignKey)
        if marcas:
            queryset = queryset.filter(marcas__nombre__icontains=marcas)

        # Filtra por tipo (ForeignKey)
        if tipo:
            queryset = queryset.filter(tipo__nombre__icontains=tipo)

        # Filtra por presentación (ForeignKey)
        if presentacion:
            queryset = queryset.filter(presentacion__descripcion__icontains=presentacion)

        # Filtra por unidad de medida (ForeignKey)
        if unidad_medida:
            queryset = queryset.filter(unidad_medida__descripcion__icontains=unidad_medida)
            
        return queryset

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

@method_decorator(never_cache, name='dispatch')
class ProductoCreateView(CreateView):

    model = Productos
    form_class = ProductosForm
    template_name = "Productos/crear.html"
    success_url = reverse_lazy('apl:listar_producto')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Crear Producto"
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
class ProductoUpdateView(UpdateView):

    model = Productos
    form_class = ProductosForm
    template_name = "Productos/crear.html"
    success_url = reverse_lazy('apl:listar_producto')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualizar Producto"
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
class ProductoDeleteView(DeleteView):

    model = Productos
    template_name = "Productos/eliminar.html"
    success_url = reverse_lazy('apl:listar_producto')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Eliminar Producto"
        context['crear_url'] = reverse_lazy('apl:listar_producto')
        return context

    def post(self, request, *args, **kwargs):
        
        try:

            response = super().delete(request, args, kwargs)
            messages.success(request, "Producto eliminado con éxito.")
            return response
            
        except ProtectedError:

            messages.error(request, f"No se ha logrado eliminar el producto.")
            return redirect(self.success_url + f"?pk={self.kwargs.get('pk')}")
        
        except Exception as e:

            messages.error(request, f"Ha ocurrido un error inesperado \n{e}")

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
