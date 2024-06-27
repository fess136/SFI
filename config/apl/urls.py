from django.urls import path
from apl.views import *
from apl.views.tipo.views import *
app_name = 'apl'
urlpatterns = [
    path('tipo/listar', TipoListView.as_view(), name = "listar_tipo"),
    path('tipo/listar2', TipoListView.as_view(), name = "listar_tipo2"),
    path('tipo/editar/<int:pk>', TipoUpdateView.as_view(), name = 'editar_tipo'),
    path('tipo/borrar/<int:pk>', TipoDeleteView.as_view(), name = "borrar_tipo"),
    path('tipo/crear', TipoCreateView.as_view(), name = "crear_tipo"),

]
