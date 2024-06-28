from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from apl.models import *

class IdentificadorListView(ListView):
    model = Tipo_identificador
    template_name = 'Tipo_identificador/listar.html'
    
class IdentificadorCreateView(CreateView):
    
    model = Tipo_identificador
    form_class = Iden
    
