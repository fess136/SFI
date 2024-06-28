from dataclasses import fields
from django.forms import *

from apl.models import *

class TipoForm(ModelForm):

    #Le agrega un poco de diseño al formulario
    class Meta:
        model = Tipo
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={'placeholder': 'Ingrese un nombre'}
            ),

        }

class MarcaForm(ModelForm):

    class Meta:
        
        model = Marcas
        fields = '__all__'

class AdministradorForm(ModelForm):

    class Meta:
        model = Administradores
        fields = '__all__'

class VentaForm(ModelForm):

    class Meta:
        model = Ventas
        fields = '__all__'

class ProductosForm(ModelForm):

    class Meta:
        model = Productos
        fields = '__all__'

class PresentacionForm(ModelForm):

    class Meta:
        model = Presentacion
        fields = '__all__'

class MedidaForm(ModelForm):

    class Meta:
        model = Unidad_Medida
        fields = '__all__'

class EmpleadoForm(ModelForm):

    class Meta:

        model = Empleados
        fields = '__all__'

class ClienteForm(ModelForm):

    class Meta:

        model = Clientes
        fields = '__all__'

class IdentificadorForm(ModelForm):

    class Meta:

        model = Tipo_identificador
        fields = '__all__'

class MetodoForm(ModelForm):

    class Meta:

        model = Metodo_Pago
        fields = '__all__'

class ProveedorForm(ModelForm):

    class Meta:

        model = Proveedores
        fields = '__all__'    

class CompraForm(ModelForm):

    class Meta:

        model = Compras
        fields = '__all__' 