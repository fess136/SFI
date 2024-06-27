from dataclasses import fields
from django.forms import *

from apl.models import Tipo

class TipoForm(ModelForm):
    
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['nombre'].widget.attrs['autofocus'] = False

    class Meta:
        model = Tipo
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={'placeholder': 'Ingrese un nombre'}
            ),

        }
