
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import ListView,CreateView
from django.shortcuts import render,redirect
from apl.models import *

from django.utils.decorators import method_decorator

def lista_tipo(request):
    
    nombre={
        'titulo':'listado de categoria',
        'tipos':Tipo.objects.all(),
    }
    return render(request,'tipo/listar.html',nombre)

# class TipoListView(ListView):
#     model = Tipo
#     template_name = 'tipo/listar.html'
    
#     # @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
        
#         if request.method == 'get':
#             return redirect('apl:tipo_lista1')
        
#         return super().dispatch(request, *args, **kwargs)

#     def get_context_data(self, **kwargs):
#         context=super().get_context_data(**kwargs)
#         context['titulo'] = 'Listado de tipos'
#         return context
    
    
