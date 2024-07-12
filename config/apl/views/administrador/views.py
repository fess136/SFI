from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.shortcuts import render
from apl.forms import AdministradorForm
from apl.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

#SE UTILIZO EL DECORADOR DE NEVER_CACHE PARA QUE NO MOSTRARA INFORMACION DE LA TABLAS CUANDO SE CERRARA SECION
@method_decorator(never_cache, name='dispatch')
class AdministradorListView(ListView):
    model = Administradores
    template_name = 'Administrador/listar.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['titulo'] = "Listar Administradores"
        context['crear_url'] = reverse_lazy('apl:crear_administrador')

        return context
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

@method_decorator(never_cache, name='dispatch')
class AdministradorCreateView(CreateView):

    model = Administradores
    form_class = AdministradorForm
    template_name = 'Administrador/crear.html'
    success_url = reverse_lazy('apl:listar_administrador')

     #decorador para proteccion de la vista desde el login

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        #Envia el tiutlo al archivo crear.html
        context['titulo'] = 'Crear Administrador'

        return context
    
    #Este metodo valida que no se repitan los datos
    def form_valid(self, form):
        # Obtener el nombre de la categoría del formulario
        cedula = form.cleaned_data.get('cedula')

        if Administradores.objects.filter(cedula__iexact=cedula).exists():
            form.add_error(
                'cedula', 'Ya existe un administrador con la misma ceula.')
            return self.form_invalid(form)

        return super().form_valid(form)
    
@method_decorator(never_cache, name='dispatch')
class AdministradorUpdateView(UpdateView):

    model = Administradores
    form_class = AdministradorForm
    template_name = "Administrador/crear.html"
    success_url = reverse_lazy('apl:listar_administrador')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Administrador'
        return context    

    #     #Este metodo valida que no se repitan los datos
    # def form_valid(self, form):
    #     # Obtener el nombre de la categoría del formulario
    #     cedula = form.cleaned_data.get('cedula')

    #     if Administradores.objects.filter(cedula__iexact=cedula).exists():
    #         form.add_error(
    #             'cedula', 'Ya existe un administrador con la misma ceula.')
    #         return self.form_invalid(form)

    #     return super().form_valid(form)

@method_decorator(never_cache, name='dispatch')
class AdministradorDeleteView(DeleteView):

    model = Administradores
    template_name = 'Administrador/eliminar.html'
    success_url = reverse_lazy('apl:listar_administrador')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Eliminar Administrador"
        context['crear_url'] = reverse_lazy('apl:listar_administrador')
        
        return context
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)