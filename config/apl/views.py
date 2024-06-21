from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
# Create your views here.

def vista1(request):
    nombres={
        
        "productos":Productos.objects.all()
    }

    return render(request,"index.html", nombres)


def vista2(request):
    
    nombre={
        
        "tipos": Tipo.objects.all()
    }
    return render(request,"categorias.html",nombre)

def vista3 (request):
    
    
    return render(request,"bootstrap.html")
