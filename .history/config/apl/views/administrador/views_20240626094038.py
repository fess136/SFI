from django.views.generic import ListView
from django.shortcuts import render
from apl.models import *

class AdministraListView(ListView):
    model = Administradores
    template_name = 'administradores/listar.html'
    
