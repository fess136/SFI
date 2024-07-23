from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render
from apl.forms import CompraForm
from apl.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


class DetalleCompraListView(ListView):

    model = DetalleCompra
    template_name = "DetalleCompra/listar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Detalle de Compra"
        context['crear_url'] = reverse_lazy('apl:crear_detallecompra')
        return context

class DetalleCompraCreateView(CreateView):

    model = DetalleCompra
    template_name = "DetalleCompra/crear.html"
    success_url = reverse_lazy("apl:listar_detallecompra")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Crear Detalle de Compra"

class DetalleCompraDeleteView(DeleteView):

    model = DetalleCompra
    template_name = "DetalleCompra/eliminar.html"
    success_url = reverse_lazy("apl:listar_detallecompra")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Eliminar Detalle de Compra"


class DetalleCompraDetailView(DetailView):

    model = DetalleCompra
    template_name = "DetalleCompra/listar.html"
    success_url = reverse_lazy("apl:listar_compra")