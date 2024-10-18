from django.http import JsonResponse
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.exceptions import ValidationError
from apl.models import Administradores
from apl.forms import AdministradorForm, TipoForm
from django.views.decorators.cache import never_cache
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
import re
from apl.models import Administradores


@method_decorator(never_cache , name='dispatch')
@method_decorator(login_required, name='dispatch')
class AdministradorListView(ListView):
    model = Administradores
    template_name = 'administrador/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Administradores'
        context['entidad'] = 'Administradores'
        context['crear_url'] = reverse_lazy('apl:crear_administrador')
        context['entidad'] = "Administradores"
        return context
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = Administradores.objects.all()

        # Captura los parámetros de la URL
        id = self.request.GET.get('id')
        user = self.request.GET.get('user')
        nombre = self.request.GET.get('nombre')
        numero_documento = self.request.GET.get('numero_documento')
        correo_electronico = self.request.GET.get('correo_electronico')
        telefono = self.request.GET.get('telefono')
        tipo_documento = self.request.GET.get('tipo_documento')

        if id:
            if int(id) >= 1:  # Verifica que el número sea positivo
                    queryset = queryset.filter(id=id)
            else:
                messages.error(self.request, "El ID no es válido.")

        # Filtra por nombre del cliente
        if user:
            if re.match("^[A-Za-zÀ-ÿ\s]+$", user):  # Verifica que solo tenga letras (incluye acentos)
                queryset = queryset.filter(user__username__icontains=user)
            else:
                messages.error(self.request, "El nombre solo debe contener letras")
        
        # Validación para apellido (solo letras)
        if nombre:
            if re.match("^[A-Za-zÀ-ÿ\s]+$", nombre):  # Verifica que solo tenga letras (incluye acentos)
                queryset = queryset.filter(nombre__icontains=nombre)
            else:
                messages.error(self.request, "El nombre solo debe contener letras")
                
        # Filtra por tipo de identificacion (ForeignKey)
        if tipo_documento:
            queryset = queryset.filter(tipo_documento__icontains=tipo_documento)
            
        # Filtra por Numero de identificacion del administrador
        if numero_documento:
            queryset = queryset.filter(numero_documento__icontains=numero_documento)
                
        # Filtra por telefono del administrador
        if telefono:
            queryset = queryset.filter(telefono__icontains=telefono)

        return queryset
    

@method_decorator(never_cache , name='dispatch')
@method_decorator(login_required, name='dispatch')
class AdministradorCreateView(CreateView):
    model = Administradores
    form_class = AdministradorForm
    template_name = 'administrador/crear.html'
    success_url = reverse_lazy('apl:listar_administrador')
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Administrador'
        context['entidad'] = 'Registrar administrador'
        context['listar_url'] = reverse_lazy('apl:listar_administrador')
        context['crear_url'] = reverse_lazy('apl:listar_administrador')
        context['formulario'] = TipoForm()
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

@method_decorator(never_cache , name='dispatch')
@method_decorator(login_required, name='dispatch')
class AdministradorUpdateView(UpdateView):
    model = Administradores
    form_class = AdministradorForm
    template_name = 'administrador/crear.html'
    success_url = reverse_lazy('apl:listar_administrador')
    

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar administrador'
        context['entidad'] = 'Editar administrador'
        context['listar_url'] = reverse_lazy('apl:listar_administrador')
        context['crear_url'] = reverse_lazy('apl:listar_administrador')
        context['formulario'] = TipoForm()
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
@method_decorator(never_cache , name='dispatch')
@method_decorator(login_required, name='dispatch')
class AdministradorDeleteView(DeleteView):
    model = Administradores
    template_name = 'administrador/eliminar.html'
    success_url = reverse_lazy('apl:listar_administrador')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar administrador'
        context['entidad'] = 'Eliminar administrador'
        context['listar_url'] = reverse_lazy('apl:listar_administrador')
        return context
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        
        try:

            response = super().delete(request, args, kwargs)
            messages.success(request, "Administrador eliminado con éxito.")
            return response
            
        except Exception as e:

            messages.error(request, f"No se ha logrado eliminado el Administrador\n{e}")
            return redirect(self.success_url)