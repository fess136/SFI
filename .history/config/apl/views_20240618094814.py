from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
# Create your views here.

def vista1(request):
    nombres={
        
        "nombre":"Fabian",
        "tipos":Productos.objects.all()
    }

    return render(request,"index.html",nombres)


def vista2(request):
    
    nombre={
        
        "nombre":"Fabian"
    }
    return JsonResponse(nombre)