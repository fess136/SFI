from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apl.forms import ProductosForm
from django.urls import reverse_lazy
from django.shortcuts import render
from apl.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


@method_decorator(never_cache, name='dispatch')
class ProductoListView(ListView):
    model = Productos
    template_name = 'Productos/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Listar Productos"
        context['crear_url'] = reverse_lazy('apl:crear_producto')
        return context
    
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
        return context
    
    def form_valid(self, form):
        # Obtener el nombre de la categoría del formulario
        nombre = form.cleaned_data.get('nombre').lower()
        cantidad = form.cleaned_data.get('cantidad')

        if Productos.objects.filter(nombre__iexact=nombre).exists():
            form.add_error(
                'nombre', 'Ya existe una categoría con este nombre.')
            return self.form_invalid(form)
        
        elif Productos.objects.filter(cantidad__iexact=cantidad).exists():

            form.add_error(
                'nombre', 'ya existe una categoría con este nombre.')

            return self.form_invalid(form)

        return super().form_valid(form)

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
        return context

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
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
