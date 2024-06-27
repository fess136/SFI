from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import ListView
from django.shortcuts import render,redirect
from apl.models import *


def lista_tipo(request):
    nombre={
        'titulo': 'listado de categorias',
        'nombre': Tipo.objects.all()
    }
    return render(request,'tipo/listar.html',nombre)
    
    
class TipoListView(ListView):
    model = Tipo
    template_name = 'tipo/listar.html'
    
    
    def dispatch(self, request, *args, **kwargs):
        
        
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de tipos'
        return context