from django.utils.deprecation import MiddlewareMixin
from .models import ClickTracking
from django.utils import timezone

class TrackLinkClickMiddleware(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):
        if 'pk' in view_kwargs:
            detalle_id = view_kwargs['pk']
            ClickTracking.objects.create(detalle_id=detalle_id, timestamp=timezone.now())
        return None
