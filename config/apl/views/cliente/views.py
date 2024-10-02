from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.db.models import ProtectedError
from django.contrib import messages
from apl.forms import ClienteForm, TipoForm
from apl.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
import re

@method_decorator(never_cache, name='dispatch')
class ClienteListView(ListView):
    model = Clientes
    template_name = 'Clientes/listar.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Clientes"
        context['crear_url'] = reverse_lazy('apl:crear_cliente')
        context['entidad'] = "Clientes"
        context['obj_relacionados'] =[i.__str__() for i in Clientes.objects.get(id = self.request.GET.get('pk')).ventas_set.all()] if self.request.GET.get('pk') else None
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

        # Filtra por Numero de identificacion del cliente
        if nit:
            queryset = queryset.filter(nit__icontains=nit)
        
        # Validación y filtrado para el correo electrónico
        if correo_electronico:
            # Si solo se ingresa un dominio, ej: 'gmail.com'
            if re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', correo_electronico):
                queryset = queryset.filter(correo_electronico__icontains=f'@{correo_electronico}')
            else:
                try:
                    validate_email(correo_electronico)  # Valida si es un correo completo
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
class ClienteCreateView(CreateView):

    model = Clientes
    form_class = ClienteForm
    template_name = "Clientes/crear.html"
    success_url = reverse_lazy('apl:listar_cliente')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Crear Cliente"
        context['crear_url'] = reverse_lazy('apl:listar_cliente')
        context['formulario'] = TipoForm()
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        cliente = form.save()
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'status': 'success',
                                 'nombre': cliente.__str__(),
                                 'id': cliente.id})
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
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
@method_decorator(never_cache, name='dispatch')
class ClienteUpdateView(UpdateView):

    model = Clientes
    form_class = ClienteForm
    template_name = "Clientes/crear.html"
    success_url = reverse_lazy('apl:listar_cliente')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualizar Cliente"
        context['crear_url'] = reverse_lazy('apl:listar_cliente')
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
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
@method_decorator(never_cache, name='dispatch')
class ClienteDeleteView(DeleteView):

    model = Clientes
    template_name = "Clientes/eliminar.html"
    success_url = reverse_lazy('apl:listar_cliente')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Eliminar Cliente"
        context['crear_url'] = reverse_lazy('apl:listar_cliente')
        return context
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        
        try:

            response = super().delete(request, args, kwargs)
            messages.success(request, "Cliente eliminado con éxito.")
            return response
            
        except ProtectedError:

            messages.error(request, f"No se ha logrado eliminar el Cliente.")
            return redirect(self.success_url + f"?pk={self.kwargs.get('pk')}")
        
        except Exception as e:

            messages.error(request, f"Ha ocurrido un error inesperado \n{e}")