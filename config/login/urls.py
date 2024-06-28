from django.urls import path 
from login.views import *

urlpatterns = [
   path('',LoginFormView.as_view(), name='login')


]