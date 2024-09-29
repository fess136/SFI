from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from apl.forms import CompraForm, MetodoForm, ProveedorForm
from django.contrib import messages
from django.db.models import ProtectedError
from apl.models import Compras
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


@method_decorator(never_cache, name='dispatch')
class ComprasListView(ListView):    
    model = Compras
    template_name = 'Compras/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Compras"
        context['crear_url'] = reverse_lazy('apl:crear_compra')
        context['entidad'] = "Compras"
        context['hay_compras_pendientes'] = Compras.objects.filter(finalizado = False)
        context['obj_relacionados'] = [i.__str__() for i in Compras.objects.get(id = self.request.GET.get('pk')).detallecompra_set.all()] if self.request.GET.get('pk') else None
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)



@method_decorator(never_cache, name='dispatch')
class CompraCreateView(CreateView):

    model = Compras
    form_class = CompraForm
    template_name = "Compras/crear.html"

    def get_success_url(self):
        return reverse_lazy('apl:crear_detallecompra', args = [Compras.objects.all().last()])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Crear Compra"
        context['formulario'] = {
            'metodo': MetodoForm(),
            'proveedor': ProveedorForm()
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
            return JsonResponse({'status': 'success', 'id': self.object.id, 'es_compra': True})
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
class CompraUpdateView(UpdateView):

    model = Compras
    form_class = CompraForm
    template_name = "Compras/crear.html"
    success_url = reverse_lazy('apl:listar_compra')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualizar Compra"
        context['crear_url'] = reverse_lazy('apl:listar_compra')
        context['formulario'] = {
            'metodo': MetodoForm(),
            'proveedor': ProveedorForm()
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
class CompraDeleteView(DeleteView):

    model = Compras
    template_name = "Compras/eliminar.html"
    success_url = reverse_lazy('apl:listar_compra')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Eliminar Compra"
        context['crear_url'] = reverse_lazy('apl:listar_compra')
        return context
    
      #decorador para proteccion de la vista desde el login
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

    
    def post(self, request, *args, **kwargs):
        
        try:

            response = super().delete(request, args, kwargs)
            messages.success(request, "Compra eliminada con éxito.")
            return response
            
        except ProtectedError:

            messages.error(request, f"No se ha logrado eliminar la Compra.")
            return redirect(self.success_url + f"?pk={self.kwargs.get('pk')}")
        
        except Exception as e:

            messages.error(request, f"Ha ocurrido un error inesperado \n{e}")