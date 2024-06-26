from django.views.generic import ListView
from django.shortcuts import render
from apl.models import *

class PresentacionListView(ListView):
    model = Presentacion
    template_name = 'presentaciones/listar.html'
    
