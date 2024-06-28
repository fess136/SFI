from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from apl.forms import MetodoForm
from apl.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class MetodosListView(ListView):
    model = Metodo_Pago
    template_name = 'Metodos_pago/listar.html'
<<<<<<< HEAD
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Listar Metodos de Pagos"
        context['crear_url'] = reverse_lazy('apl:crear_metodo')
        return context



class MetodoCreateView(CreateView):

    model = Metodo_Pago
    form_class = MetodoForm
    template_name = "Metodos_pago/crear.html"
    success_url = reverse_lazy('apl:listar_metodo')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Crear Metodos de Pago"
        return context
    
class MetodoUpdateView(UpdateView):

    model = Metodo_Pago
    form_class = MetodoForm
    template_name = "Metodos_pago/crear.html"
    success_url = reverse_lazy('apl:listar_metodo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualizar Metodos de Pago"
        return context
    
class MetodoDeleteView(DeleteView):

    model = Metodo_Pago
    template_name = "Metodos_pago/eliminar.html"
    success_url = reverse_lazy('apl:listar_metodo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Eliminar Metodos de Pago"
        context['crear_url'] = reverse_lazy('apl:listar_metodo')
        return context
=======

      #decorador para proteccion de la vista desde el login
   
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
>>>>>>> main
