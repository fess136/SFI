from django.views.generic import ListView
from django.shortcuts import render
from apl.models import *

class AdministradorListView(ListView):
    model = 
    template_name = 'marca/listar.html'
    
