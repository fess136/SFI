from django.test import TestCase
import sys
sys.path.append(str(path(__file__)))
from config.wsgi import*
from apl.models import*
# Create your tests here.
try:
    
    p=Productos.objects.get(id=3)
    print(p.nombre)
    p.nombre= "chazo"
    p.save
    
except Exception as e: