from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from apl.forms import ClienteForm
from apl.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class ClienteListView(ListView):
    model = Clientes
    template_name = 'Clientes/listar.html'
<<<<<<< HEAD
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Listar Clientes"
        context['crear_url'] = reverse_lazy('apl:crear_cliente')
        return context



class ClienteCreateView(CreateView):

    model = Clientes
    form_class = ClienteForm
    template_name = "Clientes/crear.html"
    success_url = reverse_lazy('apl:listar_cliente')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Crear Cliente"
        return context
    
class ClienteUpdateView(UpdateView):

    model = Clientes
    form_class = ClienteForm
    template_name = "Clientes/crear.html"
    success_url = reverse_lazy('apl:listar_cliente')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualizar Cliente"
        return context
    
class ClienteDeleteView(DeleteView):

    model = Clientes
    template_name = "Clientes/eliminar.html"
    success_url = reverse_lazy('apl:listar_cliente')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Eliminar Cliente"
        context['crear_url'] = reverse_lazy('apl:listar_cliente')
        return context
=======
      #decorador para proteccion de la vista desde el login
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
>>>>>>> main
