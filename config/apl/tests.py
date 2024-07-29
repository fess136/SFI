from django.test import TestCase
import sys
from pathlib import Path

from django.urls import reverse_lazy
sys.path.append(str(Path(__file__).parent.parent))
from config.wsgi import*
from apl.models import*

# Create your tests here.
# a = 
# print(Productos.objects.filter(id=DetalleCompra.objects.filter(id=1).producto.id).precio)
print(Compras.objects.filter(id = 5))
try:

        p = Productos.objects.get(id=4)
                
        # p.nombre = "loca"
        # p.save()
        # print(p.nombre)

except Exception as e:
        print("Oscar es gay")
        
