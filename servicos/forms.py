from django import forms
from .models import Servicos

class ServicosModelForm(forms.ModelForm):
    class Meta:
        model = Servicos
        fields = '__all__'