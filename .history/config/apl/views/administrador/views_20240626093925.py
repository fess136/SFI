from django.views.generic import ListView
from django.shortcuts import render
from apl.models import *

class MarcaListView(ListView):
    model = ad
    template_name = 'marca/listar.html'
    
