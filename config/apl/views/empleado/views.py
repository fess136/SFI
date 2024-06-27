from django.views.generic import ListView
from django.shortcuts import render
from apl.models import *

class EmpleListView(ListView):
    model = Empleados
    template_name = 'Empleados/listar.html'
    
