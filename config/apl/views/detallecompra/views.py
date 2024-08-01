from django.db.models.query import QuerySet
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from apl.forms import CompraForm
from apl.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

from apl.forms import DetalleCompraForm


class DetalleCompraCreateView(CreateView):

    model = DetalleCompra
    form_class = DetalleCompraForm
    template_name = "DetalleCompra/crear.html"

    def get_success_url(self):
        # Obtén el último ID de la tabla Compras
        ultimo_id = Compras.objects.values_list('id', flat=True).last()
        return reverse_lazy('apl:detallar_detallecompra', args=[ultimo_id])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Crear Detalle de Compra"
        return context

class DetalleCompraDeleteView(DeleteView):

    model = DetalleCompra
    template_name = "DetalleCompra/eliminar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Eliminar Detalle de Compra"
        return context
    
    def get_success_url(self):
        
        return reverse_lazy('apl:detallar_detallecompra', args=[DetalleCompra.objects.get(id = self.kwargs.get('pk')).compra])



class DetalleCompraUpdateView(UpdateView):

    model = DetalleCompra
    form_class = DetalleCompraForm
    template_name = "DetalleCompra/crear.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Editar Detalle de Compra"
        return context

    def get_success_url(self):
        
        return reverse_lazy('apl:detallar_detallecompra', args=[DetalleCompra.objects.get(id = self.kwargs.get('pk')).compra])

@method_decorator(never_cache, name='dispatch')
class DetalleCompraDetailView(DetailView):

    model = Compras
    template_name = "DetalleCompra/listar.html"
    context_object_name = "objeto"
    success_url = reverse_lazy("apl:listar_compra")
    
    def post(self,  request, *args, **kwargs):

        accion = request.POST.get('accion')

        if accion == "finalizar":

            DetalleCompra.objects.filter(compra = self.kwargs.get('pk')).update(finalizado = True)

            return redirect('apl:listar_compra')

        return redirect('apl:detallar_detallecompra', pk=self.kwargs.get('pk'))



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entidad'] = "DetalleCompras"
        context['crear_url'] = reverse_lazy('apl:crear_detallecompra')
        context['id'] = self.kwargs.get('pk')
        context['compra'] = Compras.objects.get(id = self.kwargs.get('pk'))
        context['finalizo'] = DetalleCompra.objects.filter(finalizado = True, compra = self.kwargs.get('pk')).exists()
        context['precio_total_compra'] = sum([j.precio_total_por_registro() for j in [i for i in DetalleCompra.objects.filter(compra = self.kwargs.get('pk'))]])

        return context