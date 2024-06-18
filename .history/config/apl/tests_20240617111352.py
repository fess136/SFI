from django.test import TestCase
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from config.wsgi import*
from apl.models import*
# Create your tests here.

p = Productos(nombre="zz",cantidad=100,precio=500,marcas_id=1,presentacion_id=1,tipo_id=1,unidad_medida_id=1).save()
# try:

#         p = Productos.objects.get(id=3)
#         print(p.nombre)
#         p.nombre = "tonto"
#         p.save()
        

# except Exception as e:
#     print("Oscar es gay")
