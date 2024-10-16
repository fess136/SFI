
from typing import Any
from django.http import HttpRequest, JsonResponse
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from django.contrib import messages
from django.shortcuts import render


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
class LoginFormView(LoginView):
     
     template_name = 'login.html'
     def loginview(request):
          if request.method == 'POST':
               form = LoginForm(request.POST)
               if form.is_valid():
                    username = form.cleaned_data.get('username')
                    password = form.cleaned_data.get('password')
               user = authenticate(request, username=username, password=password)
               if user is not None:
                    login(request, user)
                    return redirect('dashboard')  # Redirige a la página de inicio después del login
               else:
                    form.add_error(None, 'Nombre de usuario o contraseña incorrectos')
          else:
               form = LoginForm()

          return render(request, 'login.html', {'form': form})

class logoutredirect(RedirectView):
     
     pattern_name="login"  
     
     def dispatch(self, request, *args, **kwargs) :
          logout(request)
          
          return super().dispatch(request, *args, **kwargs)

def validate_email(request):
    email = request.GET.get('email', None)
    response = {
        'is_taken': User.objects.filter(email__iexact=email).exists()
    }
    return JsonResponse(response)