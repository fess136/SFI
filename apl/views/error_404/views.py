from django.views.generic import TemplateView

class Error404view(TemplateView):
    template_name = 'error_404.html'