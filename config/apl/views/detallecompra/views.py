from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render
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
    success_url = reverse_lazy("apl:listar_detallecompra")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Eliminar Detalle de Compra"


class DetalleCompraDetailView(DetailView):

    model = Compras
    template_name = "DetalleCompra/listar.html"
    context_object_name = "objeto"
    success_url = reverse_lazy("apl:listar_compra")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['crear_url'] = reverse_lazy('apl:crear_detallecompra')

        return context