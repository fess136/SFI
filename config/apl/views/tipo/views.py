from django.http import JsonResponse
from apl.forms import TipoForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import ProtectedError
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from apl.models import *
from apl.forms import TipoForm

import re

@method_decorator(never_cache, name='dispatch')
class TipoCreateView(CreateView):

    model = Tipo
    form_class = TipoForm
    template_name = 'tipo/crear.html'
    success_url = reverse_lazy('apl:listar_tipo')

    # #valida que no se repitan los datos
    # def form_valid(self, form):
    #     # Obtener el nombre de la categoría del formulario
    #     nombre = form.cleaned_data.get('nombre').lower()

    #     if Tipo.objects.filter(nombre__iexact=nombre).exists():
    #         form.add_error(
    #             'nombre', 'Ya existe una categoría con este nombre.')
    #         return self.form_invalid(form)

    #     return super().form_valid(form)

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'status': 'success'})
        return response

    def form_invalid(self, form):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            errors = {}
            for field, error_list in form.errors.items():
                errors[field] = [str(error) for error in error_list]
            return JsonResponse({
                'status': 'error',
                'errors': errors
            }, status=400)
        return super().form_invalid(form)
    
      #decorador para proteccion de la vista desde el login
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        #Envia el tiutlo al archivo crear.html
        context['titulo'] = 'Crear Tipo'
        context['crear_url'] = reverse_lazy('apl:listar_tipo')
        return context
        

    
@method_decorator(never_cache, name='dispatch')
class TipoDeleteView(DeleteView):

    model = Tipo
    template_name = 'tipo/eliminar.html'
    success_url = reverse_lazy('apl:listar_tipo')

      #decorador para proteccion de la vista desde el login

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

    #Metodo para exportar variables a el template tipo/eliminar.html
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['crear_url'] = reverse_lazy('apl:listar_tipo')
        context['titulo'] = "Eliminar Tipo"

        return context
    
    def post(self, request, *args, **kwargs):
        
        try:

            response = super().delete(request, args, kwargs)
            messages.success(request, "Tipo eliminado con éxito.")
            return response
            
        except ProtectedError:

            messages.error(request, f"No se ha logrado eliminar el Tipo.")
            return redirect(self.success_url + f"?pk={self.kwargs.get('pk')}")
        
        except Exception as e:

            messages.error(request, f"Ha ocurrido un error inesperado \n{e}")
    

@method_decorator(never_cache, name='dispatch')
class TipoUpdateView(UpdateView):
    
    model = Tipo
    form_class = TipoForm
    template_name = "tipo/crear.html"
    success_url = reverse_lazy('apl:listar_tipo')

      #decorador para proteccion de la vista desde el login

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

    #Metodo para exportar variables a el template tipo/crear.html
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualizar Tipo"
        context['crear_url'] = reverse_lazy('apl:listar_tipo')
        return context 

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'status': 'success'})
        return response

    def form_invalid(self, form):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            errors = {}
            for field, error_list in form.errors.items():
                errors[field] = [str(error) for error in error_list]
            return JsonResponse({
                'status': 'error',
                'errors': errors
            }, status=400)
        return super().form_invalid(form)


@method_decorator(never_cache, name='dispatch')
class TipoListView(ListView):

    model = Tipo
    template_name = 'tipo/listar.html'

      #decorador para proteccion de la vista desde el login
    
    # @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

    #Metodo para exportar variables a el template tipo/listar.html
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['titulo'] = "Tipo"
        context['crear_url'] = reverse_lazy('apl:crear_tipo')
        context['obj_relacionados'] = [i.__str__() for i in Tipo.objects.get(id = self.request.GET.get('pk')).productos_set.all()] if self.request.GET.get('pk') else None
        context['entidad'] = 'Tipos'

        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        # Obtiene los parámetros de consulta de la URL
        id = self.request.GET.get('id')
        nombre = self.request.GET.get('nombre')
        estado = self.request.GET.get('estado')

        # Filtra los resultados según los parámetros proporcionados
        if id:
            if int(id) >= 1:  # Verifica que el número sea positivo
                    queryset = queryset.filter(id=id)
            else:
                messages.error(self.request, "El ID debe ser un número válido.")
                
        if nombre:
            if re.match("^[A-Za-z0-9\s]+$", nombre):  # Solo letras, números y espacios
                queryset = queryset.filter(nombre__icontains=nombre)
            else:
                messages.error(self.request, "El nombre no puede contener caracteres especiales.")
                
        if estado:
                queryset = queryset.filter(estado__iexact=estado)  # Filtra por estado
        return queryset

