from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

def vista1(request):
    nombre={
        
        "nombre":"Fabian"
    }

    return render(request,"index.html")


def vista2(request):
    
    nombre={
        
        "nombre":"Fabian"
    }
    return JsonResponse(nombre)
