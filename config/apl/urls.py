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
from apl.views.producto.views import *
from apl.views.proveedor.views import *

from apl.views.medidas.views import*
from apl.views.ventas.views import*
app_name = 'apl'
urlpatterns = [

    #Modulo Tipo
    path('tipos/listar', TipoListView.as_view(), name = "listar_tipo"),
    path('tipos/listar2', TipoListView.as_view(), name = "listar_tipo2"),
    path('tipos/editar/<int:pk>', TipoUpdateView.as_view(), name = 'editar_tipo'),
    path('tipos/borrar/<int:pk>', TipoDeleteView.as_view(), name = "borrar_tipo"),
    path('tipos/crear', TipoCreateView.as_view(), name = "crear_tipo"),

    #Modulo Presentacion
    path("presentaciones/listar",PresentacionListView.as_view(), name="listar_presentacion"),

    #Modulo Marcas
    path('marcas/listar', MarcaListView.as_view(), name = "listar_marca"),

    #Modulo Administrador
    path('administradores/listar', AdministradorListView.as_view(), name="listar_administrador"),

    #Modulo Marcas
    path('empleados/listar', EmpleListView.as_view(), name="listar_empleado"),

    #Modulo Metodos
    path('metodos/listar', MetodosListView.as_view(), name="listar_metodo"),

    #Modulo Clientes
    path('clientes/listar', ClienteListView.as_view(), name="listar_cliente"),

    #Modulo Compras
    path('compras/listar',ComprasListView.as_view(), name = "listar_compras"),

    #Modulo Productos
    path('productos/listar', ProductoListView.as_view(), name = "listar_productos"),

    #Modulo Proveedores
    path('proveedores/listar', ProveedorListView.as_view(), name = "lista_proveedor"),

    #Modulo Indentificadores
    path('identificadores/listar', IdentificadorListView.as_view(), name = "listar_compras"),

    #Modulo Medidas
    path('medidas/listar',MedidasListView.as_view(),name = "listar_medidas"),

    #Modulo Ventas
    path('ventas/listar',VentasListView.as_view(),name = "listar_ventas")
]
