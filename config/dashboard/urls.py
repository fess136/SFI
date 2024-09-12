from django.urls import path
from config.dashboard.views import *

urlpatterns = [
    path('', dashView.as_view(), name='dashboard')
]
