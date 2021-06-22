from django import forms

from tarefas.models import Tarefas


class TarefasModelForms(forms.ModelForm):
    class Meta:
        model = Tarefas
        fields = '__all__'