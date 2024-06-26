from typing import Any
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http.response import HttpResponse, JsonResponse
from django.views.generic import ListView, CreateView
from django.shortcuts import render, redirect
from apl.models import *
from apl.forms import TipoForm

def listar_tipo(request):

    return render(request, "tipo/listar.html", {"dato": Tipo.objects.all()});

class TipoCreateView(CreateView):

    model = Tipo
    form_class = TipoForm
    template_name = 'tipo/crear.html'
    success_url = reverse_lazy('apl:listar_tipo')

from django.utils.decorators import method_decorator

def lista_tipo(request):
    
    nombre={
        'titulo':'listado de categoria',
        'tipos':Tipo.objects.all(),
    }
    return render(request,'tipo/listar.html',nombre)

class TipoListView(ListView):
    model = Tipo
    template_name = 'tipo/listar.html'

    @method_decorator(login_required)
    # @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):

        if(request.method == 'GET'):

            return redirect('apl:listar_tipo2')

        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
    
        return JsonResponse({"nombre": ""})
