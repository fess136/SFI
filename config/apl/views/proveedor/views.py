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


@method_decorator(never_cache, name='dispatch')
class ProveedorListView(ListView):
    model = Proveedores
    template_name = 'Proveedores/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Proveedores"
        context['crear_url'] = reverse_lazy('apl:crear_proveedor')
        context['entidad'] = "Proveedores"
        context['obj_relacionados'] = [i.__str__() for i in Proveedores.objects.get(id = self.request.GET.get('pk')).compras_set.all()] if self.request.GET.get('pk') else None
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

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