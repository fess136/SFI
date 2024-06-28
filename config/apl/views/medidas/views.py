from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render
from apl.forms import MedidaForm
from apl.models import *

class MedidasListView(ListView):
    model = Unidad_Medida
    template_name = 'Unidades_medida/listar.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Listar Unidades de Medida"
        context['crear_url'] = reverse_lazy('apl:crear_medida')
        return context

class MedidaCreateView(CreateView):

    model = Unidad_Medida
    form_class = MedidaForm
    template_name = "Unidades_medida/crear.html"
    success_url = reverse_lazy('apl:listar_medida')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Crear Unidad de Medida"
        return context
    
class MedidaUpdateView(UpdateView):

    model = Unidad_Medida
    form_class = MedidaForm
    template_name = "Unidades_medida/crear.html"
    success_url = reverse_lazy('apl:listar_medida')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualizar Unidad de Medida"
        return context
    
class MedidaDeleteView(DeleteView):

    model = Unidad_Medida
    template_name = "Unidades_medida/eliminar.html"
    success_url = reverse_lazy('apl:listar_medida')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Eliminar Unidad de Medida"
        context['crear_url'] = reverse_lazy('apl:listar_medida')
        return context