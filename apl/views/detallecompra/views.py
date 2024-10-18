from django.db.models.query import QuerySet
from django.http import Http404, JsonResponse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.core.serializers.json import DjangoJSONEncoder
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import ProtectedError
from apl.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

from apl.forms import DetalleCompraForm, ProductosForm

@method_decorator(never_cache, name='dispatch')
class DetalleCompraCreateView(CreateView):

    model = DetalleCompra
    form_class = DetalleCompraForm
    template_name = "DetalleCompra/crear.html"

    def get_success_url(self):

        return reverse_lazy('apl:detallar_detallecompra', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Crear Detalle de Compra"
        context['crear_url'] = self.get_success_url() 
        context['formulario'] = ProductosForm()
        return context
    
    def obtener_precio(request):

        id_producto = request.GET.get('id')
        try:
            producto = Productos.objects.get(id = id_producto)
            data = {'precio': int(producto.precio)}
            return JsonResponse(data, encoder=DjangoJSONEncoder)
        except Productos.DoesNotExist:

            return JsonResponse({'error', 'Producto no encontrado'}, status=404)
    
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

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['id_compra'] = self.kwargs.get('pk')

        return kwargs
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
@method_decorator(never_cache, name='dispatch')
class DetalleCompraDeleteView(DeleteView):

    model = DetalleCompra
    template_name = "DetalleCompra/eliminar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Eliminar Detalle de Compra"
        return context
    
    def get_success_url(self):
        
        return reverse_lazy('apl:detallar_detallecompra', args=[DetalleCompra.objects.get(id = self.kwargs.get('pk')).compra])
    
    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            messages.error(request, 'El detalle de compra no existe o ya ha sido eliminado.')
            return redirect(reverse_lazy('apl:listar_compra'))
            
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        
        try:

            response = super().delete(request, args, kwargs)
            messages.success(request, "Detalle de compra eliminada con éxito.")
            return response
            
        except ProtectedError:

            messages.error(request, f"No se ha logrado eliminar el detalle de compra.")
            return redirect(self.success_url + f"?pk={self.kwargs.get('pk')}")
        
        except Exception as e:

            messages.error(request, f"Ha ocurrido un error inesperado \n{e}")

@method_decorator(never_cache, name='dispatch')
class DetalleCompraUpdateView(UpdateView):

    model = DetalleCompra
    form_class = DetalleCompraForm
    template_name = "DetalleCompra/crear.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Editar Detalle de Compra"
        context['formulario'] = ProductosForm()
        context['crear_url'] = reverse_lazy('apl:detallar_detallecompra', args=[DetalleCompra.objects.get(id = self.kwargs.get('pk')).compra.id])
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
    

    def get_success_url(self):
        
        return reverse_lazy('apl:detallar_detallecompra', args=[DetalleCompra.objects.get(id = self.kwargs.get('pk')).compra.id])

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

@method_decorator(never_cache, name='dispatch')
class DetalleCompraDetailView(DetailView):

    model = Compras
    template_name = "DetalleCompra/listar.html"
    context_object_name = "objeto"
    success_url = reverse_lazy("apl:listar_compra")
    
    def post(self,  request, *args, **kwargs):

        accion = request.POST.get('accion')

        if accion == "finalizar":

            #Cada vez que se presione el boton finalizar compra, la misma tendra el estado compra finalizada
            Compras.objects.filter(id = self.kwargs.get('pk')).update(finalizado = True)
            
            #Aqui se actualiza la cantidad de cada uno de los productos seleccionados en la compra
            for i in DetalleCompra.objects.filter(compra = self.kwargs.get('pk')):

                Productos.objects.filter(id = i.producto.id).update(cantidad = i.producto.cantidad + i.cantidad)

            return redirect('apl:listar_compra')

        return redirect('apl:detallar_detallecompra', pk=self.kwargs.get('pk'))



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entidad'] = "DetalleCompras"
        context['crear_url'] = reverse_lazy('apl:crear_detallecompra', args = [self.kwargs.get('pk')])
        context['compra'] = Compras.objects.get(id = self.kwargs.get('pk'))
        context['finalizo'] = Compras.objects.filter(finalizado = True, id = self.kwargs.get('pk')).exists() # Valida si la compra se finalizo para mostrar o no botones
        context['Total'] = sum([j.Total() for j in [i for i in DetalleCompra.objects.filter(compra = self.kwargs.get('pk'))]]) # Muestra El precio total
        context['hay_productos'] = DetalleCompra.objects.filter(compra = self.kwargs.get('pk')).exists() # Valida si hay productos agregados al detalle de compra

        return context
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)