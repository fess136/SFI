from django.views.generic import ListView
from django.shortcuts import render
from apl.models import *

class PresentacionListView(ListView):
    model = Marcas
    template_name = 'marca/listar.html'
    
