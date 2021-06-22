from django import forms
from .models import Diario

class DiarioModelForm(forms.ModelForm):
    class Meta:
        model = Diario
        fields = '__all__'