from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.url import reverse_lazy
from django.shortcuts import render
from apl.forms import TipoIdentificadorForm
from apl.models import *

class IdentificadorListView(ListView):
    model = Tipo_identificador
    template_name = 'Tipo_identificador/listar.html'
    
class IdentificadorCreateView(CreateView):
    
    model = Tipo_identificador
    form_class = Tipo
    template_name = 'Tipo_Identificador/crear.html'
    success_url = reverse_lazy('apl:listar_identificador')
    
    def get
    
