
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
# Create your views here.

class LoginFormView(LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
            if request.user.is_authenticated:
             return redirect('apl:listar_tipo' )
            return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['titulo']='iniciar sesion'
           
         return context
    

    