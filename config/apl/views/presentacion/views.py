from django.views.generic import ListView
from django.shortcuts import render
from apl.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class PresentacionListView(ListView):
    model = Presentacion
    template_name = 'Presentaciones/listar.html'

      #decorador para proteccion de la vista desde el login
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
