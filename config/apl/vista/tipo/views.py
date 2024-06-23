from django.shortcuts import render
from apl.models import Tipo

def listar_tipo(request):

    elementos = {

        "titulo": "Listar Tipos", #titulo de la tabla
        "datos": Tipo.objects.all() #datos de la tabla tipos
        
        }

    return render(request, "Tipo/listar.html", elementos)