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
from apl.views.detallecompra.views import *

app_name = 'apl'
urlpatterns = [

    #Modulo Tipo
    path('tipos/listar/', TipoListView.as_view(), name = "listar_tipo"),
    path('tipos/editar/<int:pk>', TipoUpdateView.as_view(), name = 'editar_tipo'),
    path('tipos/borrar/<int:pk>', TipoDeleteView.as_view(), name = "borrar_tipo"),
    path('tipos/crear', TipoCreateView.as_view(), name = "crear_tipo"),

    #Modulo Presentacion
    path("presentaciones/listar",PresentacionListView.as_view(), name="listar_presentacion"),
    path("presentaciones/crear", PresentacionCreateView.as_view(), name = "crear_presentacion"),
    path("presentaciones/editar/<int:pk>", PresentacionUpdateView.as_view(), name = "editar_presentacion"),
    path("presentaciones/borrar/<int:pk>", PresentacionDeleteView.as_view(), name = "borrar_presentacion"),

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
    path('empleados/listar', EmpleadoListView.as_view(), name="listar_empleado"),
    path('empleados/crear', EmpleadoCreateView.as_view(), name = "crear_empleado"),
    path('empleados/editar/<int:pk>', EmpleadoUpdateView.as_view(), name = "editar_empleado"),
    path('empleados/borrar/<int:pk>', EmpleadoDeleteView.as_view(), name = "borrar_empleado"),

    #Modulo Metodos
    path('metodos/listar', MetodosListView.as_view(), name="listar_metodo"),
    path('metodos/crear', MetodoCreateView.as_view(), name = "crear_metodo"),
    path('metodos/editar/<int:pk>', MetodoUpdateView.as_view(), name = "editar_metodo"),
    path('metodos/borrar/<int:pk>', MetodoDeleteView.as_view(), name = "borrar_metodo"),

    #Modulo Clientes
    path('clientes/listar', ClienteListView.as_view(), name="listar_cliente"),
    path('clientes/crear', ClienteCreateView.as_view(), name = "crear_cliente"),
    path('clientes/editar/<int:pk>', ClienteUpdateView.as_view(), name = "editar_cliente"),
    path('clientes/borrar/<int:pk>', ClienteDeleteView.as_view(), name = "borrar_cliente"),

    #Modulo Compras
    path('compras/listar',ComprasListView.as_view(), name = "listar_compra"),
    path('compras/crear', CompraCreateView.as_view(), name = "crear_compra"),
    path('compras/editar/<int:pk>', CompraUpdateView.as_view(), name = 'editar_compra'),
    path('compras/borrar/<int:pk>', CompraDeleteView.as_view(), name = "borrar_compra"),

    #Detalle de Compras

    path('detallecompras/detallar', DetalleCompraDetailView.as_view(), name = "detallar_compra"),
    path('detallecompras/crear', DetalleCompraCreateView.as_view, name = "crear_detallecompra"),
    path('detallecompras/borrar', DetalleCompraDetailView.as_view(), name = "borrar_detallecompra"),

    #Modulo Productos
    path('productos/listar', ProductoListView.as_view(), name = "listar_producto"),
    path('productos/crear', ProductoCreateView.as_view(), name = "crear_producto"),
    path('productos/editar/<int:pk>', ProductoUpdateView.as_view(), name = "editar_producto"),
    path('productos/borrar/<int:pk>', ProductoDeleteView.as_view(), name = "borrar_producto"),

    #Modulo Proveedores
    path('proveedores/listar', ProveedorListView.as_view(), name = "listar_proveedor"),
    path('proveedores/crear', ProveedorCreateView.as_view(), name = "crear_proveedor"),
    path('proveedores/editar/<int:pk>', ProveedorUpdateView.as_view(), name = "editar_proveedor"),
    path('proveedores/borrar/<int:pk>', ProveedorDeleteView.as_view(), name = "borrar_proveedor"),

    #Modulo Indentificadores
    path('identificadores/listar', IdentificadorListView.as_view(), name = "listar_identificador"),
    path('identificadores/crear', IdentificadorCreateView.as_view(), name = "crear_identificador"),
    path('identificadores/editar/<int:pk>', IdentificadorUpdateView.as_view(), name = "editar_identificador"),
    path('identificadores/borrar/<int:pk>', IdentificadorDeleteView.as_view(), name = "borrar_identificador"),

    #Modulo Medidas
    path('medidas/listar',MedidasListView.as_view(),name = "listar_medida"),
    path('medidas/crear', MedidaCreateView.as_view(), name = 'crear_medida'),
    path('medidas/editar/<int:pk>', MedidaUpdateView.as_view(), name = 'editar_medida'),
    path('medidas/borrar/<int:pk>', MedidaDeleteView.as_view(), name = 'borrar_medida'),

    #Modulo Ventas
    path('ventas/listar',VentasListView.as_view(),name = "listar_venta"),
    path('ventas/crear', VentaCreateView.as_view(), name = 'crear_venta'),
    path('ventas/editar/<int:pk>', VentaUpdateView.as_view(), name = 'editar_venta'),
    path('ventas/borrar/<int:pk>', VentaDeleteView.as_view(), name = 'borrar_venta')
    
]
