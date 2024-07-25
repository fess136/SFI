from django.test import TestCase
import sys
from pathlib import Path

from django.urls import reverse_lazy
sys.path.append(str(Path(__file__).parent.parent))
from config.wsgi import*
from apl.models import*

# Create your tests here.

p = Productos(nombre="zz",cantidad=100,precio=500,marcas_id=1,presentacion_id=1,tipo_id=1,unidad_medida_id=1).save()
# a = 
print([i[0] for i in list(Compras.objects.values_list('id', flat=False))][-1])
try:

        p = Productos.objects.get(id=4)
                
        # p.nombre = "loca"
        # p.save()
        # print(p.nombre)

except Exception as e:
        print("Oscar es gay")
        
