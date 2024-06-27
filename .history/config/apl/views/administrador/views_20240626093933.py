from django.views.generic import ListView
from django.shortcuts import render
from apl.models import *

class MarcaListView(ListView):
    model = Administradores
    template_name = '/listar.html'
    
