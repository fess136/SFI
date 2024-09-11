from django.http import JsonResponse
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import ProtectedError
from django.urls import reverse_lazy
from apl.forms import VentaForm
from apl.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
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
@method_decorator(never_cache, name='dispatch')
class VentaCreateView(CreateView):

    model = Ventas
    form_class = VentaForm
    template_name = "Ventas/crear.html"
    success_url = reverse_lazy('apl:crear_detalleventa', args=[0])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Crear Venta"
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
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
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
            messages.success(request, "Tipo de identificador eliminado con éxito.")
            return response
            
        except ProtectedError:

            messages.error(request, f"No se ha logrado eliminar el Tipo de identificador.")
            return redirect(self.success_url + f"?pk={self.kwargs.get('pk')}")
        
        except Exception as e:

            messages.error(request, f"Ha ocurrido un error inesperado \n{e}")