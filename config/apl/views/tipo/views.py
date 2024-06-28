from typing import Any
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http.response import HttpResponse, JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        #Envia el tiutlo al archivo crear.html
        context['titulo'] = 'Crear Tipo'
        context['crear_url'] = reverse_lazy('apl:crear_tipo')

        return context
    
    #Este metodo valida que no se repitan los datos
    def form_valid(self, form):
        # Obtener el nombre de la categoría del formulario
        nombre = form.cleaned_data.get('nombre').lower()

        if Tipo.objects.filter(nombre__iexact=nombre).exists():
            form.add_error(
                'nombre', 'Ya existe una categoría con este nombre.')
            return self.form_invalid(form)

        return super().form_valid(form)
    
class TipoDeleteView(DeleteView):

    model = Tipo
    template_name = 'tipo/eliminar.html'
    success_url = reverse_lazy('apl:listar_tipo')

    #Metodo para exportar variables a el template tipo/eliminar.html
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['crear_url'] = reverse_lazy('apl:listar_tipo')
        context['titulo'] = "Eliminar Tipo"

        return context

class TipoUpdateView(UpdateView):
    
    model = Tipo
    form_class = TipoForm
    template_name = "tipo/crear.html"
    success_url = reverse_lazy('apl:listar_tipo')

    #Metodo para exportar variables a el template tipo/crear.html
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualizar Tipo"
        return context 

    #valida que no se repitan los datos
    def form_valid(self, form):
        # Obtener el nombre de la categoría del formulario
        nombre = form.cleaned_data.get('nombre').lower()

        if Tipo.objects.filter(nombre__iexact=nombre).exists():
            form.add_error(
                'nombre', 'Ya existe una categoría con este nombre.')
            return self.form_invalid(form)

        return super().form_valid(form)

class TipoListView(ListView):

    model = Tipo
    template_name = 'tipo/listar.html'

    #Metodo para exportar variables a el template tipo/listar.html
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['titulo'] = "Listar Tipo"
        context['crear_url'] = reverse_lazy('apl:crear_tipo')
        context['entidad'] = 'Tipos'

        return context

    def post(self, request, *args, **kwargs):
        return JsonResponse({'nombre': "Oscar"})
    
    # @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
