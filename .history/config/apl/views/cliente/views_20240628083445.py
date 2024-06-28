from django.views.generic import ListView ,CreateView, UpdateView, DeleteView
from django.shortcuts import render
from apl.models import *
from django.urls import reverse_lazy
from apl.forms import Clienteform

 
class ClienteListView(ListView):
    model = Clientes
    template_name = 'Clientes/listar.html'
    