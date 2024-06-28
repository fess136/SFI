from django.views.generic import ListView
from django.shortcuts import render
from apl.models import *

class ListView(ListView):
    model = Administradores
    template_name = 'Administradores/listar.html'
    
