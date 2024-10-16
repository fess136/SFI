from django.contrib import messages
from django.db.models.query import QuerySet
from django.http import Http404, HttpRequest, HttpResponse, JsonResponse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from apl.forms import DetalleVentaForm, ProductosForm
from apl.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

@method_decorator(never_cache, name='dispatch')
class DetalleVentaDetailView(DetailView):

    model = Ventas
    template_name = "DetalleVenta/listar.html"
    context_object_name = "objeto"
    success_url = reverse_lazy("apl:listar_venta")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Listar Detalle de Venta"
        context['id'] = self.kwargs.get('pk')
        context['detalle_venta'] = DetalleVenta.objects.all()
        context['hay_productos'] = DetalleVenta.objects.filter(venta = self.kwargs.get('pk')).exists()
        context['Total'] = sum(i.Total() for i in DetalleVenta.objects.filter(venta = self.kwargs.get('pk')))
        context['venta'] = Ventas.objects.get(id = self.kwargs.get('pk'))
        context['finalizo'] = Ventas.objects.filter(finalizado = True, id = self.kwargs.get('pk')).exists()

        return context
    
    def post(self, request, *args, **kwargs):
        if request.POST.get('accion') == "finalizar":
            try:
                errores = []
                for i in DetalleVenta.objects.filter(venta=self.kwargs.get('pk')):
                    producto = Productos.objects.get(id=i.producto.id)
                    
                    if i.cantidad > producto.cantidad:
                        errores.append(f"id: {producto.id} - Producto: {producto.nombre}")
                        
                if errores:

                    raise ValidationError(errores)

                # Se queda la venta finalizada
                Ventas.objects.filter(id=self.kwargs.get('pk')).update(finalizado=True)

                # se actualiza los productos en stock
                for i in DetalleVenta.objects.filter(venta=self.kwargs.get('pk')):
                    Productos.objects.filter(id=i.producto.id).update(
                        cantidad=i.producto.cantidad - i.cantidad
                    )

                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({'status': 'success'})
                else:
                    return redirect('apl:listar_venta')

            except ValidationError as e:
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({'status': 'error', 'message': ', '.join(e)}, status=400)
                
            return redirect('apl:listar_detalleventa', args=[self.kwargs.get('pk')])
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

@method_decorator(never_cache, name='dispatch')
class DetalleVentaCreateView(CreateView):

    model = DetalleVenta
    form_class = DetalleVentaForm
    template_name = "DetalleVenta/crear.html"
    
    def get_success_url(self):
        return reverse_lazy('apl:listar_detalleventa', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Crear Detalle de Venta"
        context['crear_url'] = self.get_success_url()
        context['formulario'] = ProductosForm()

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
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['id_venta'] = self.kwargs.get('pk')

        return kwargs

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

@method_decorator(never_cache, name='dispatch')
class DetalleVentaUpdateView(UpdateView):

    model = DetalleVenta
    form_class = DetalleVentaForm
    template_name = "DetalleVenta/crear.html"

    def get_success_url(self):
        return reverse_lazy('apl:listar_detalleventa', args = [DetalleVenta.objects.get(id = self.kwargs.get('pk')).venta])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Editar Detalle de Venta"
        context['formulario'] = ProductosForm()
        context['crear_url'] = reverse_lazy('apl:listar_detalleventa', args = [DetalleVenta.objects.get(id = self.kwargs.get('pk')).venta])
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
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['hay_edicion'] = True
        kwargs['id'] = self.kwargs.get('pk')
        return kwargs

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

@method_decorator(never_cache, name='dispatch')
class DetalleVentaDeleteView(DeleteView):

    model = DetalleVenta
    template_name = "DetalleVenta/eliminar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Eliminar Detalle de Venta"
    

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            messages.error(request, 'El detalle de venta no existe o ya ha sido eliminado.')
            return redirect(reverse_lazy('apl:listar_venta'))

    def get_success_url(self):
        
        return reverse_lazy('apl:listar_detalleventa', args=[DetalleVenta.objects.get(id = self.kwargs.get('pk')).venta])

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
