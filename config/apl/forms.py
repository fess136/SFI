from dataclasses import fields
from django.forms import *
from django import forms
from apl.models import *

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, Select, NumberInput, EmailInput, PasswordInput
from apl.models import Administradores

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
    username = forms.CharField(label="Usuario", max_length=150)
    email = forms.EmailField(label="Correo", max_length=150)
    password = forms.CharField(label="Password", widget=PasswordInput)
    conf_password = forms.CharField(label="Confirm Password", widget=PasswordInput)

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        self.fields["nombre"].widget.attrs["autofocus"] = True

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password1 = cleaned_data.get("password")
        password2 = cleaned_data.get("conf_password")

        if User.objects.filter(username=username).exists():
            raise ValidationError("Este nombre de usuario ya está en uso.")
        
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este correo electrónico ya está en uso.")
        
        if not password2:
            raise ValidationError("Necesitas validar tu contraseña")
        
        if password1 != password2:
            raise ValidationError("Las contraseñas no coinciden")
        
        return cleaned_data

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if User.objects.filter(username=username).exists():
            raise ValidationError("Este nombre de usuario ya está en uso.")
        
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este correo electrónico ya está en uso.")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        administrador = super().save(commit=False)
        administrador.user = user
        administrador.contrasena = password 
        administrador.conf_contrasena = cleaned_data.get('conf_password')
        if commit:
            administrador.save()
        return administrador

    class Meta:
        model = Administradores
        fields = ["username", "email", "nombre", "tipo_documento", "numero_documento", "telefono", "password", "conf_password"]
        widgets = {
            "nombre": TextInput(attrs={"placeholder": "Nombre del administrador"}),
            "tipo_documento": Select(attrs={"placeholder": "Tipo de documento"}),
            "numero_documento": NumberInput(attrs={"min": 8, "placeholder": "Número de documento"}),
            "telefono": NumberInput(attrs={"min": 1, "placeholder": "Teléfono"}),
            "password": PasswordInput(attrs={"min": 1, "placeholder": "Contraseña"}),
            "conf_password": PasswordInput(attrs={"min": 1, "placeholder": "Confirme su contraseña"})
        }
class VentaForm(ModelForm):

    class Meta:
        model = Ventas
        fields = ['usuario', 'cliente', 'metodo_pago']

    def __init__(self, *args, **kwargs):

        self.usuario = kwargs.pop('usuario',None)

        super().__init__(*args, **kwargs)
        self.fields['usuario'].initial = self.usuario
        self.fields['usuario'].disabled = True
        

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


class ClienteForm(ModelForm):

    class Meta:

        model = Clientes
        fields = '__all__'

class IdentificadorForm(forms.ModelForm):
    class Meta:
        model = Tipo_identificador
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Si este formulario se usa para seleccionar un Tipo_identificador en otro modelo,
        # asegúrate de que solo se muestren las opciones activas
        if 'instance' not in kwargs:
            self.fields['tipo_identificador'] = forms.ModelChoiceField(
                queryset=Tipo_identificador.activos.all(),
                empty_label="Seleccione un tipo de identificador",
                required=False
            )

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
        fields = ['usuario', 'metodo_pago', 'proveedor']
    
    def __init__(self, *args, **kwargs):

        self.usuario = kwargs.pop('usuario',None)

        super().__init__(*args, **kwargs)
        self.fields['usuario'].initial = self.usuario
        self.fields['usuario'].disabled = True



class DetalleCompraForm(ModelForm):

    class Meta:
        
        model = DetalleCompra
        fields = ['compra', 'cantidad', 'producto', 'precio_unitario']

    def __init__(self, *args, **kwargs):

        self.id_compra = kwargs.pop('id_compra', None)
        
        super().__init__(*args, **kwargs)

        self.fields['compra'].initial = self.id_compra
        self.fields['compra'].disabled = True

        
    def clean_fixed_value(self):
        return self.id_compra
    
class DetalleVentaForm(ModelForm):

    class Meta:

        model =  DetalleVenta
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        
        self.id_venta = kwargs.pop("id_venta",  None)
        self.id_detalle = kwargs.pop('id', None)

        self.edicion = kwargs.pop('hay_edicion', None)

        super().__init__(*args, **kwargs)

        self.fields['venta'].initial = self.id_venta
        self.fields['venta'].disabled = True
        
    def clean_fixed_value(self):
        return self.id_venta
    
    def clean(self):

        campos = super().clean()

        id = campos.get('venta')
        cantidad = campos.get('cantidad')
        producto = campos.get('producto')

        # si es para agregar un nuevo detalle de venta se hace la validacion para que no se repita el producto
        if not self.edicion:
            if DetalleVenta.objects.filter(venta = id, producto = Productos.objects.get(id= producto.id).id).exists():

                self.add_error("producto", f"{producto} ya existe en esta compra, ya puede ser editado en la tabla")

        # pero si se esta editando valida que no se ingrese un producto que ya habia sido ingresado a excepcion del que se habia
        # registrado en ese detalle de venta
        elif self.edicion and producto != DetalleVenta.objects.get(id = self.id_detalle).producto:

            if DetalleVenta.objects.filter(venta = id, producto = producto.id).exists():

                self.add_error("producto", f"{producto} ya existe en este detalle de venta")

        
        if cantidad > Productos.objects.get(id = producto.id).cantidad:

            
            self.add_error("cantidad", f"Quieres vender {cantidad} productos pero solo hay {Productos.objects.get(nombre = producto).cantidad} productos en stock")