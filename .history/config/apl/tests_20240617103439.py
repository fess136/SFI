from django.test import TestCase
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from config.wsgi import*
from apl.models import*
# Create your tests here.
try:

        p = Productos.objects.get(id=3)
        print(p.nombre)
        p.nombre = "tonto"
        p.save()
        

except Exception as e:
    print("Oscar es gay")
