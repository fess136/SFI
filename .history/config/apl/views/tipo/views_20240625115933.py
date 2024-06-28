
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import ListView
from django.shortcuts import render,redirect
from apl.models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class TipoListView(ListView):
    model = Tipo
    template_name = 'tipo/listar.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        
        if request.method == 'get':
            return redirect('apl:tipo_lista1')
        
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de tipos'
        return context