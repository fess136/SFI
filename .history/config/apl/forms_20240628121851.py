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

class TipoIdentificadorForm(ModelForm):
    
    class Meta:
        
        model = Tipo_identificador
        fields = '__all__'

class Clienteform(ModelForm):
    class Meta:
        model = Clientes
        fields = '__all__'


        
class MetodoPagoForm(ModelForm):
    class Meta:
        model = Metodo_Pago
        fields = '__all__'