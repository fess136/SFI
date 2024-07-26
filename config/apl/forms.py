from dataclasses import fields
from django.forms import *
from django import forms

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

class DetalleCompraForm(ModelForm):

    class Meta:
        
        model = DetalleCompra
        fields = '__all__'

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['compra'].initial = Compras.objects.all()[len(Compras.objects.all())-1]
        self.fields['compra'].disabled = True
        
    def clean_fixed_value(self):
        return Compras.objects.all()[len(Compras.objects.all())-1]