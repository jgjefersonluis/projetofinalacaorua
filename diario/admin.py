from django.contrib import admin

from django.contrib import admin

from .models import Diario


@admin.register(Diario)
class DiarioAdmin(admin.ModelAdmin):
    list_display = ('data', 'hora', 'local', 'profissional', 'acao', 'sujeitos', 'avaliacao')
