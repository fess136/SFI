from django.test import TestCase
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from config.wsgi import*
from apl.models import*
# Create your tests here.


try:

        p = Productos.objects.get(id=4)
        print(p.nombre)
        # p.nombre = "loca"
        # p.save()
        # print(p.nombre)

except Exception as e:
    print("Oscar es gay")
