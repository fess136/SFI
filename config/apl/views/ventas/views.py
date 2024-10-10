from django.http import JsonResponse
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import ProtectedError, Q
from django.urls import reverse_lazy
from apl.forms import VentaForm, ClienteForm, MetodoForm
from apl.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

import re
from datetime import datetime, timedelta

#
@method_decorator(never_cache, name='dispatch')
class VentasListView(ListView):
    model = Ventas
    template_name = 'Ventas/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Ventas"
        context['crear_url'] = reverse_lazy('apl:crear_venta')
        context['obj_relacionados'] = [i.__str__() for i in Ventas.objects.get(id = self.request.GET.get('pk')).detalleventa_set.all()] if self.request.GET.get('pk') else None
        context['entidad'] = "Ventas"
        context['hay_ventas_pendientes'] = Ventas.objects.filter(finalizado = False)
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = super().get_queryset()

        # Captura los parámetros de la URL
        id = self.request.GET.get('id')
        fecha_desde = self.request.GET.get('fecha_desde')
        fecha_hasta = self.request.GET.get('fecha_hasta')
        usuario = self.request.GET.get('usuario')
        cliente_nombre_o_apellido = self.request.GET.get('cliente')
        metodo_pago_nombre = self.request.GET.get('metodo_pago')
        finalizado = self.request.GET.get('finalizado')

        # Filtrar por ID
        if id:
            try:
                id = int(id)
                if id >= 1:
                    queryset = queryset.filter(id=id)
                else:
                    messages.error(self.request, "El ID debe ser un número positivo.")
            except ValueError:
                messages.error(self.request, "El ID debe ser un número válido.")

        # Filtrar por rango de fechas
        if fecha_desde:
            try:
                fecha_desde = datetime.strptime(fecha_desde, '%Y-%m-%d')
                queryset = queryset.filter(fecha_venta__gte=fecha_desde)
            except ValueError:
                messages.error(self.request, "El formato de la fecha 'desde' no es válido.")

        if fecha_hasta:
            try:
                fecha_hasta = datetime.strptime(fecha_hasta, '%Y-%m-%d')
                # Añadir 23 horas, 59 minutos y 59 segundos a la fecha_hasta
                fecha_hasta = fecha_hasta + timedelta(days=1) - timedelta(seconds=1)
                queryset = queryset.filter(fecha_venta__lte=fecha_hasta)
            except ValueError:
                messages.error(self.request, "El formato de la fecha 'hasta' no es válido.")
        
        if metodo_pago_nombre:
            if re.match("^[A-Za-z0-9\s]+$", metodo_pago_nombre):  # Solo letras, números y espacios
                queryset = queryset.filter(metodo_pago__nombre__icontains = metodo_pago_nombre)
            else:
                messages.error(self.request, "El metodo de pago no puede contener caracteres especiales")

        # Filtrar por usuario
        if usuario:
            if re.match("^[A-Za-z0-9\s]+$", usuario):  # Solo letras, números y espacios
                queryset = queryset.filter(usuario=usuario)
            else:
                messages.error(self.request, "El usuario no puede contener caracteres especiales")

        # Filtrar por cliente (ForeignKey)
        if cliente_nombre_o_apellido:
            if re.match("^[A-Za-zÀ-ÿ\s]+$", cliente_nombre_o_apellido):  # Verifica que solo tenga letras (incluye acentos)
                queryset = queryset.filter(
                    Q(cliente__nombre__icontains=cliente_nombre_o_apellido) |
                    Q(cliente__apellido__icontains=cliente_nombre_o_apellido)
                )
            else:
                messages.error(self.request, "El nombre del cliente solo debe contener letras")


        # Filtrar por estado (finalizado)
        if finalizado:
            finalizado = finalizado.lower() == 'true'
            queryset = queryset.filter(finalizado=finalizado)

        return queryset
    
@method_decorator(never_cache, name='dispatch')
class VentaCreateView(CreateView):

    model = Ventas
    form_class = VentaForm
    template_name = "Ventas/crear.html"
    success_url = reverse_lazy('apl:crear_detalleventa', args=[0])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Crear Venta"
        context['formulario'] = {
            'cliente': ClienteForm(),
            'metodo': MetodoForm()
        }
        return context
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['usuario'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        response = super().form_valid(form)
        self.object = form.save()
        print(self.object.id)
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'status': 'success', 'id': self.object.id, 'es_venta': True})
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
class VentaUpdateView(UpdateView):

    model = Ventas
    form_class = VentaForm
    template_name = "Ventas/crear.html"
    success_url = reverse_lazy('apl:listar_venta')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualizar Venta"
        context['crear_url'] = self.success_url
        context['formulario'] = {
            'cliente': ClienteForm(),
            'metodo': MetodoForm()
        }
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
class VentaDeleteView(DeleteView):

    model = Ventas
    template_name = "Ventas/eliminar.html"
    success_url = reverse_lazy('apl:listar_venta')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Eliminar Venta"
        context['crear_url'] = reverse_lazy('apl:listar_venta')
        return context
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        
        try:

            response = super().delete(request, args, kwargs)
            messages.success(request, "venta eliminada con éxito.")
            return response
            
        except ProtectedError:

            messages.error(request, f"No se ha logrado eliminar la venta.")
            return redirect(self.success_url + f"?pk={self.kwargs.get('pk')}")
        
        except Exception as e:

            messages.error(request, f"Ha ocurrido un error inesperado \n{e}")