from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import ProtectedError
from apl.forms import ProveedorForm
from apl.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
import re

@method_decorator(never_cache, name='dispatch')
class ProveedorListView(ListView):
    model = Proveedores
    template_name = 'Proveedores/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Proveedores"
        context['crear_url'] = reverse_lazy('apl:crear_proveedor')
        context['entidad'] = "Proveedores"
        context['obj_relacionados'] = ', '.join([i.__str__() for i in Proveedores.objects.get(id = self.request.GET.get('pk')).compras_set.all()]) if self.request.GET.get('pk') else None
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = super().get_queryset()

        # Captura los parámetros de la URL
        id = self.request.GET.get('id')
        nombre = self.request.GET.get('nombre')
        apellido = self.request.GET.get('apellido')
        nit = self.request.GET.get('nit')
        ubicacion = self.request.GET.get('ubicacion')
        correo_electronico = self.request.GET.get('correo_electronico')
        telefono = self.request.GET.get('telefono')
        Tipo_identificador = self.request.GET.get('Tipo_identificador')

        if id:
            if int(id) >= 1:  # Verifica que el número sea positivo
                    queryset = queryset.filter(id=id)
            else:
                messages.error(self.request, "El ID debe ser un número positivo.")

        # Filtra por nombre del cliente
        if nombre:
            if re.match("^[A-Za-zÀ-ÿ\s]+$", nombre):  # Verifica que solo tenga letras (incluye acentos)
                queryset = queryset.filter(nombre__icontains=nombre)
            else:
                messages.error(self.request, "El nombre solo debe contener letras")
        
        # Validación para apellido (solo letras)
        if apellido:
            if re.match("^[A-Za-zÀ-ÿ\s]+$", apellido):  # Verifica que solo tenga letras (incluye acentos)
                queryset = queryset.filter(apellido__icontains=apellido)
            else:
                messages.error(self.request, "El apellido solo debe contener letras")
                
                # Validación para ubicacion (solo letras)
        if ubicacion:
            if re.match("^[A-Za-zÀ-ÿ\s]+$", ubicacion):  # Verifica que solo tenga letras (incluye acentos)
                queryset = queryset.filter(ubicacion__icontains=ubicacion)
            else:
                messages.error(self.request, "La ubicacion solo debe ser una ciudad")

        # Filtra por Numero de identificacion del cliente
        if nit:
            queryset = queryset.filter(nit__icontains=nit)

        # Filtra por correo electronico
        if correo_electronico:
            try:
                validate_email(correo_electronico)  # Usa la validación de Django para formato general
                # Verificar el dominio del correo
                domain = correo_electronico.split('@')[-1]
                valid_domains = ['gmail.com', 'hotmail.com']  # Ajusta los dominios permitidos
                if domain not in valid_domains:
                    messages.error(self.request, f"El dominio {domain} no es válido. Use un dominio permitido.")
                else:
                    queryset = queryset.filter(correo_electronico__icontains=correo_electronico)
            except ValidationError:
                messages.error(self.request, "El correo electrónico no es válido.")
                
        # Filtra por telefono del cliente
        if telefono:
            queryset = queryset.filter(telefono__icontains=telefono)

        # Filtra por tipo de identificacion (ForeignKey)
        if Tipo_identificador:
            queryset = queryset.filter(Tipo_identificador__nombre__icontains=Tipo_identificador)
            
        return queryset

@method_decorator(never_cache, name='dispatch')
class ProveedorCreateView(CreateView):

    model = Proveedores
    form_class = ProveedorForm
    template_name = "Proveedores/crear.html"
    success_url = reverse_lazy('apl:listar_proveedor')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Crear Proveedor"
        context['crear_url'] = self.success_url
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
       
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
@method_decorator(never_cache, name='dispatch')
class ProveedorUpdateView(UpdateView):

    model = Proveedores
    form_class = ProveedorForm
    template_name = "Proveedores/crear.html"
    success_url = reverse_lazy('apl:listar_proveedor')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualizar Proveedor"
        context['crear_url'] = self.success_url
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
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

@method_decorator(never_cache, name='dispatch')
class ProveedorDeleteView(DeleteView):

    model = Proveedores
    template_name = "Proveedores/eliminar.html"
    success_url = reverse_lazy('apl:listar_proveedor')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Eliminar Proveedor"
        context['crear_url'] = reverse_lazy('apl:listar_proveedor')
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        
        try:

            response = super().delete(request, args, kwargs)
            messages.success(request, "Proveedor eliminado con éxito.")
            return response
            
        except ProtectedError:

            messages.error(request, f"No se ha logrado eliminar el Proveedor.")
            return redirect(self.success_url + f"?pk={self.kwargs.get('pk')}")
        
        except Exception as e:

            messages.error(request, f"Ha ocurrido un error inesperado \n{e}")