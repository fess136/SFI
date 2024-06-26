from django.urls import path

from apl.views.tipo.views import *
from apl.views.marca.views import *
from apl.views.presentacion.views import*
app_name = 'apl'
urlpatterns = [
<<<<<<< HEAD
    
    path('tipo/listar', TipoListView.as_view(), name = "listar_tipo"),
    path('marca/listar',MarcaListView.as_view(), name= "listar_marca"),
    
    
=======
    path('tipo/listar', TipoListView.as_view(), name = "listar_tipo"),
    path('tipo/listar2', listar_tipo, name = "listar_tipo2"),
    
    path('tipo/crear', TipoCreateView.as_view(), name = "crear_tipo"),

>>>>>>> 79e1bf1ff28031d7d46d29ddbe8d17d78e825d87
]
