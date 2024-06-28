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
    path('marcas/crear', MarcaCreateView.as_view(), name = 'crear_marca'),
    path('marcas/editar/<int:pk>', MarcaUpdateView.as_view(), name = "editar_marca"),
    path('marcas/borrar/<int:pk>', MarcaDeleteView.as_view(), name = 'borrar_marca'),

    #Modulo Administrador
    path('administradores/listar', AdministradorListView.as_view(), name="listar_administrador"),
    path('administradores/crear', AdministradorCreateView.as_view(), name = "crear_administrador"),
    path('administradores/editar/<int:pk>', AdministradorUpdateView.as_view(), name = "editar_administrador"),
    path('administradores/borrar/<int:pk>', AdministradorDeleteView.as_view(), name = 'borrar_administrador'),

    #Modulo Empleados
    path('empleados/listar', EmpleListView.as_view(), name="listar_empleado"),

    #Modulo Metodos
    path('metodos/listar', MetodosListView.as_view(), name="listar_metodo"),

    #Modulo Clientes
    path('clientes/listar', ClienteListView.as_view(), name="listar_cliente"),

    #Modulo Compras
    path('compras/listar',ComprasListView.as_view(), name = "listar_compra"),

    #Modulo Productos
    path('productos/listar', ProductoListView.as_view(), name = "listar_producto"),

    #Modulo Proveedores
    path('proveedores/listar', ProveedorListView.as_view(), name = "lista_proveedor"),

    #Modulo Indentificadores
    path('identificadores/listar', IdentificadorListView.as_view(), name = "listar_identificador"),
    path('identificadores/crear', IdentificadorCreateView.as_view(), name = 'crear_identificador'),
    path("identificador/editar", IdentificadorUpdateView.as_view(), name =),

    #Modulo Medidas
    path('medidas/listar',MedidasListView.as_view(),name = "listar_medida"),

    #Modulo Ventas
    path('ventas/listar',VentasListView.as_view(),name = "listar_venta")
]
