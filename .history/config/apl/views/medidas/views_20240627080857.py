from django.views.generic import ListView
from django.shortcuts import render
from apl.models import *

class ListView(ListView):
    model = Unidad_Medida
    template_name = 'Unidades_medida/listar.html'
    
