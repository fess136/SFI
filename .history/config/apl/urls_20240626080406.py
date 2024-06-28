from django.urls import path

from apl.views.tipo.views import *
from apl.views.marca.views import *
from apl.views.presentacion.views import*
app_name = 'apl'
urlpatterns = [
    
    path('tipo/listar', TipoListView.as_view(), name = "listar_tipo"),
    path('marca/listar',MarcaListView.as_view(), name= "listar_marca"),
    path("pres/listar",PresentacionListView.a, name="listar_presentacion")
    
]
