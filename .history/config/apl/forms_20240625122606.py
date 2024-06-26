from dataclasses import fields
from django.forms import ModelForm

from config.apl.models import Tipo

class TipoForm(ModelForm):
    class Meta:
        model= Tipo
        fields = '__all__'