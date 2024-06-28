from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apl.forms import ProductosForm
from django.urls import reverse_lazy
from django.shortcuts import render
from apl.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class ProductoListView(ListView):
    model = Productos
    template_name = 'Productos/listar.html'

<<<<<<< HEAD
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Listar Productos"
        context['crear_url'] = reverse_lazy('apl:crear_producto')
        return context



class ProductoCreateView(CreateView):

    model = Productos
    form_class = ProductosForm
    template_name = "Productos/crear.html"
    success_url = reverse_lazy('apl:listar_producto')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Crear Producto"
        return context
    
class ProductoUpdateView(UpdateView):

    model = Productos
    form_class = ProductosForm
    template_name = "Productos/crear.html"
    success_url = reverse_lazy('apl:listar_producto')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualizar Producto"
        return context
    
class ProductoDeleteView(DeleteView):

    model = Productos
    template_name = "Productos/eliminar.html"
    success_url = reverse_lazy('apl:listar_producto')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Eliminar Producto"
        context['crear_url'] = reverse_lazy('apl:listar_producto')
        return context
=======
      #decorador para proteccion de la vista desde el login

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
>>>>>>> main
