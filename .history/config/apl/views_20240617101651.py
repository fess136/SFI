from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

def vista1(request):
    
    return HttpResponse("esta es mi primera url ")


def vista2(request):
    
    nombre={
        
        "nombre":"Fabian"
    }
    return JsonResponse(nombre)
