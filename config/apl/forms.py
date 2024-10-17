from dataclasses import fields
from django.forms import *
from django.contrib import admin
from django import forms
from apl.models import *
from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, Select, NumberInput, EmailInput, PasswordInput
from apl.models import Administradores

import re

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


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nombre"].widget.attrs["autofocus"] = True
        
        # Si estamos editando un administrador existente
        if self.instance and self.instance.pk:
            # Prellenamos los campos con la información actual
            self.fields['username'].initial = self.instance.user.username
            self.fields['email'].initial = self.instance.user.email

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password1 = cleaned_data.get("contrasena")
        password2 = cleaned_data.get("conf_contrasena")

        # Verificamos si es una edición
            
        if password1:
            # Verificar longitud mínima
            
            # Verificar mayúsculas
            if not re.search(r'[A-Z]', password1):
                raise ValidationError({'contrasena':"La contraseña debe contener al menos una letra mayúscula."})
            
            # Verificar minúsculas
            if not re.search(r'[a-z]', password1):
                raise ValidationError({'contrasena':"La contraseña debe contener al menos una letra minúscula."})

        if self.instance and self.instance.pk:
            # Para edición, permitimos el mismo username y email del usuario actual
            username_exists = User.objects.filter(username=username).exclude(pk=self.instance.user.pk).exists()
            email_exists = User.objects.filter(email=email).exclude(pk=self.instance.user.pk).exists()
        else:
            # Para creación, verificamos que no exista ningún usuario con ese username o email
            username_exists = User.objects.filter(username=username).exists()
            email_exists = User.objects.filter(email=email).exists()

        if username_exists:
            raise ValidationError("Este nombre de usuario ya está en uso.")
        
        if email_exists:
            raise ValidationError("Este correo electrónico ya está en uso.")
        
        # Solo validamos las contraseñas si se proporcionaron (requerido en creación, opcional en edición)
        if password1 or password2:
            if not password2:
                raise ValidationError("Necesitas validar tu contraseña")
            
            if password1 != password2:
                raise ValidationError("Las contraseñas no coinciden")
        elif not self.instance.pk:  # Si es una creación nueva y no hay contraseña
            raise ValidationError("La contraseña es requerida para crear un nuevo administrador")
        
        return cleaned_data

    def save(self, commit=True):
        administrador = super().save(commit=False)
        cleaned_data = self.cleaned_data
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('contrasena')

        if self.instance and self.instance.pk:
            # Actualizar usuario existente
            user = self.instance.user
            user.username = username
            user.email = email
            if password:  # Solo actualizamos la contraseña si se proporcionó una nueva
                user.set_password(password)
                administrador.contrasena = password
                administrador.conf_contrasena = cleaned_data.get('conf_contrasena')
            user.save()
        else:
            # Crear nuevo usuario
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            administrador.user = user
            administrador.contrasena = password
            administrador.conf_contrasena = cleaned_data.get('conf_contrasena')

        if commit:
            administrador.save()
        return administrador

    class Meta:
        model = Administradores
        fields = ["username", "email", "nombre", "tipo_documento", "numero_documento", "telefono", "contrasena", "conf_contrasena"]
        widgets = {
            "nombre": TextInput(attrs={"placeholder": "Nombre del administrador"}),
            "tipo_documento": Select(attrs={"placeholder": "Tipo de identificación"}),
            "numero_documento": NumberInput(attrs={"min": 8, "placeholder": "Número de documento"}),
            "telefono": NumberInput(attrs={"min": 1, "placeholder": "Teléfono"}),
            "contrasena": PasswordInput(attrs={"placeholder": "Contraseña"}),
            "conf_contrasena": PasswordInput(attrs={"placeholder": "Confirme su contraseña"})
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
        widgets = {
            'id' : NumberInput(attrs={'class': 'form-control'}),
            'nombre': TextInput(attrs={'class': 'form-control'}),
            'marcas': Select(attrs={'class': 'form-control'}),
            'tipo': Select(attrs={'class': 'form-control'}),
            'presentacion': Select(attrs={'class': 'form-control'}),
            'unidad_medida': Select(attrs={'class': 'form-control'})
        }

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
        fields = ['compra', 'producto', 'cantidad', 'precio_unitario']

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

            
            self.add_error("cantidad", f"Quieres vender {cantidad} productos pero solo hay {Productos.objects.get(id = producto.id).cantidad} productos en stock")