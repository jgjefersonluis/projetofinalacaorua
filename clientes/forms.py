from django import forms
from .models import Clientes

class ClientesModelForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = '__all__'