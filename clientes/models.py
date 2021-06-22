from django.db import models


class Clientes(models.Model):
    nome = models.CharField('Nome', max_length=100)
    aniversario = models.DateField('Data de Nascimento')
    idade = models.IntegerField()
    cpf = models.CharField('CPF', max_length=11)
    escolaridade = models.CharField('Escolaridade', max_length=100)
    genero = models.CharField('Genero', max_length=30)
    etnia = models.CharField('Etnia', max_length=50)
    natural = models.CharField('Natural', max_length=100)
    spa = models.CharField('SPA', max_length=100)
    beneficios = models.CharField('Beneficios', max_length=100)
    temporua = models.CharField('Tempo na Rua', max_length=25)
    datacadastro = models.DateField('Data do Cadastro')
    profissional = models.CharField('Profissional', max_length=100)

    def __str__(self):
        return self.nome
