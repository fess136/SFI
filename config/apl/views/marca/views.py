from typing import Any
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apl.forms import MarcaForm
from apl.models import *

class MarcaListView(ListView):
    model = Marcas
    template_name = 'marca/listar.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Listar Marcas"
        context['crear_url'] = reverse_lazy('apl:crear_marca')
        return context

class MarcaCreateView(CreateView):

    model = Marcas
    form_class = MarcaForm
    template_name = "Marca/crear.html"
    success_url = reverse_lazy('apl:listar_marca')

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo'] = "Crear Marca"

        return context

        #valida que no se repitan los datos
    def form_valid(self, form):
        # Obtener el nombre de la categoría del formulario
        nombre = form.cleaned_data.get('nombre').lower()

        if Marcas.objects.filter(nombre__iexact=nombre).exists():
            form.add_error(
                'nombre', 'Ya existe una marca con este nombre.')
            return self.form_invalid(form)

        return super().form_valid(form)

class MarcaUpdateView(UpdateView):

    model = Marcas
    form_class = MarcaForm
    template_name = 'Marca/crear.html'
    success_url = reverse_lazy('apl:listar_marca')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualizar Marca"
        return context
    
class MarcaDeleteView(DeleteView):

    model = Marcas
    template_name = "Marca/eliminar.html"
    success_url = reverse_lazy('apl:listar_marca')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Marca'
        return context