from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views import View
from django.db.models import Sum, F
from django.db.models.functions import TruncMonth
from apl.models import DetalleVenta, DetalleCompra
from datetime import datetime

@method_decorator(never_cache, name='dispatch')
class dashView(TemplateView):
    
    template_name = 'dashboard.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Administración'
        return context
def get(self, request, *args, **kwargs):
        # Obtenemos el año actual
        current_year = datetime.now().year

        # Ventas
        ventas_data = DetalleVenta.objects.filter(venta_fecha_venta_year=current_year) \
            .annotate(month=TruncMonth('venta__fecha_venta')) \
            .values('month') \
            .annotate(total=Sum(F('cantidad') * F('producto__precio'))) \
            .order_by('month')

        # Compras
        compras_data = DetalleCompra.objects.filter(compra_fecha_compra_year=current_year) \
            .annotate(month=TruncMonth('compra__fecha_compra')) \
            .values('month') \
            .annotate(total=Sum(F('cantidad') * F('producto__precio'))) \
            .order_by('month')

        # Combinar ventas y compras por mes
        transaction_data = {}
        for venta in ventas_data:
            month = venta['month'].strftime('%b').upper()
            transaction_data[month] = {'month': month, 'ventas': float(venta['total']), 'compras': 0}
        for compra in compras_data:
            month = compra['month'].strftime('%b').upper()
            if month in transaction_data:
                transaction_data[month]['compras'] = float(compra['total'])
            else:
                transaction_data[month] = {'month': month, 'ventas': 0, 'compras': float(compra['total'])}

        return JsonResponse({
            'transactions': list(transaction_data.values())
        })