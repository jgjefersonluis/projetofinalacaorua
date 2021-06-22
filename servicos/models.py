from django.db import models

# Create your models here.

class Servicos(models.Model):


    data = models.DateField('Data')
    turno = models.CharField('Turno', max_length=30)
    profissional = models.CharField('Profissional', max_length=100)
    nome = models.CharField('Nome', max_length=100)
    acao = models.CharField('Ação', max_length=100)
    demanda = models.CharField('Demanda', max_length=100)
    encaminhamento = models.CharField('Encaminhamento', max_length=100)
    logradouro = models.CharField('Logradouro', max_length=100)
    observacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome