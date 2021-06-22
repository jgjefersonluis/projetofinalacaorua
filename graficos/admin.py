from django.contrib import admin

# Register your models here.
from graficos.models import Beneficio, Substancias, FaixaEtaria, Etnia, Saude, Genero


class BeneficioAdmin(admin.ModelAdmin):
    list_display = ('name', 'population')


admin.site.register(Beneficio, BeneficioAdmin)


class GeneroAdmin(admin.ModelAdmin):
    list_display = ('name', 'population')


admin.site.register(Genero, GeneroAdmin)


class SaudeAdmin(admin.ModelAdmin):
    list_display = ('name', 'population')


admin.site.register(Saude, SaudeAdmin)


class EtniaAdmin(admin.ModelAdmin):
    list_display = ('name', 'population')


admin.site.register(Etnia, EtniaAdmin)


class FaixaEtariaAdmin(admin.ModelAdmin):
    list_display = ('name', 'population')


admin.site.register(FaixaEtaria, FaixaEtariaAdmin)

class SubstanciasAdmin(admin.ModelAdmin):
    list_display = ('name', 'population')


admin.site.register(Substancias, SubstanciasAdmin)