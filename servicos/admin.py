from django.contrib import admin

from .models import Servicos


@admin.register(Servicos)
class ServicosAdmin(admin.ModelAdmin):
    list_display = ('data', 'turno', 'profissional', 'nome', 'acao', 'demanda', 'encaminhamento', 'logradouro', 'observacoes')
