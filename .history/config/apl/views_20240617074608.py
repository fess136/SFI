from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def vista1(request):
    
    return HttpResponse("esta es mi primera url ")

