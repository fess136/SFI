from django.http.request import HttpRequest as HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.exceptions import ValidationError
from apl.models import Administradores
from apl.forms import AdministradorForm
from django.views.decorators.cache import never_cache
@method_decorator(never_cache , name='dispatch')
@method_decorator(login_required, name='dispatch')
class AdministradorListView(ListView):
    model = Administradores
    template_name = 'administrador/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Administradores'
        context['entidad'] = 'Administradores'
        context['crear_url'] = reverse_lazy('apl:crear_administrador')
        return context
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    

@method_decorator(never_cache , name='dispatch')
@method_decorator(login_required, name='dispatch')
class AdministradorCreateView(CreateView):
    model = Administradores
    form_class = AdministradorForm
    template_name = 'administrador/crear.html'
    success_url = reverse_lazy('apl:listar_administrador')
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Administrador'
        context['entidad'] = 'Registrar administrador'
        context['listar_url'] = reverse_lazy('apl:listar_administrador')
        return context

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ValidationError as e:
            form.add_error(None, e)
            return self.form_invalid(form)

@method_decorator(never_cache , name='dispatch')
@method_decorator(login_required, name='dispatch')
class AdministradorUpdateView(UpdateView):
    model = Administradores
    form_class = AdministradorForm
    template_name = 'administrador/crear.html'
    success_url = reverse_lazy('apl:listar_administrador')
    

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar administrador'
        context['entidad'] = 'Editar administrador'
        context['listar_url'] = reverse_lazy('apl:listar_administrador')
        return context
    
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

@method_decorator(never_cache , name='dispatch')
@method_decorator(login_required, name='dispatch')
class AdministradorDeleteView(DeleteView):
    model = Administradores
    template_name = 'administrador/eliminar.html'
    success_url = reverse_lazy('apl:listar_administrador')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar administrador'
        context['entidad'] = 'Eliminar administrador'
        context['listar_url'] = reverse_lazy('apl:listar_administrador')
        return context
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)