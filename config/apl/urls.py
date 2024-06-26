from django.urls import path
from apl.views import *
from apl.views.tipo.views import *
app_name = 'apl'
urlpatterns = [
    path('tipo/listar', TipoListView.as_view(), name = "listar_tipo"),
    path('tipo/listar2', listar_tipo, name = "listar_tipo2"),
    path('tipo/crear', TipoCreateView.as_view(), name = "crear_tipo"),

]
