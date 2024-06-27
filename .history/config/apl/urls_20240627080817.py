from django.urls import path

from apl.views.tipo.views import *
from apl.views.marca.views import *
from apl.views.presentacion.views import*
from apl.views.administrador.views import*
from apl.views.empleado.views import *
from apl.views.metodo_pago.views import *
from apl.views.tipo_identificador.views import*
from apl.views.cliente.views import*
from apl.views.compra.views import*
app_name = 'apl'
urlpatterns = [

    path('tipo/listar', TipoListView.as_view(), name = "listar_tipo"),
    path('tipo/listar2', listar_tipo, name = "listar_tipo2"),
    path('tipo/crear', TipoCreateView.as_view(), name = "crear_tipo"),
    path("presentacion/listar",PresentacionListView.as_view(), name="listar_presentacion"),
    path('marcas/listar', MarcaListView.as_view(), name = "listar_marca"),
    path('administrador/listar', AdministradorListView.as_view(), name="listar_administrador"),
    path('empleado/listar', EmpleListView.as_view(), name="listar_empleado"),
    path('metodos/listar', MetodosListView.as_view(), name="listar_metodo"),

    path('clientes/listar', ClienteListView.as_view(), name="listar_cliente"),
    path('compras/listar',ComprasListView.as_view(), name = "listar_compras"),
    path('identificadores/listar', IdentificadorListView.as_view(), name = "listar_compras")
    
]
