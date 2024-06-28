from django.views.generic import ListView ,CreateView, UpdateView, DeleteView
from django.shortcuts import render
from apl.models import *
from django.urls import reverse_lazy
from apl.forms import Clienteform

 
class ClienteListView(ListView):
    model = Clientes
    template_name = 'Clientes/listar.html'
    

class ClienteCreateView(CreateView):
    
    model = Clientes
    form_class = Clienteform
    template_name = 'Clientes/crear.html'
    success_url = reverse_lazy('apl:')