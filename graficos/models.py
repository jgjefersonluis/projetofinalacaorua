from django.db import models

# Create your models here.

class Beneficio(models.Model):
    name = models.CharField(max_length=30)
    population = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class FaixaEtaria(models.Model):
    name = models.CharField(max_length=30)
    population = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Etnia(models.Model):
    name = models.CharField(max_length=30)
    population = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Genero(models.Model):
    name = models.CharField(max_length=30)
    population = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Saude(models.Model):
    name = models.CharField(max_length=30)
    population = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Substancias(models.Model):
    name = models.CharField(max_length=30)
    population = models.PositiveIntegerField()

    def __str__(self):
        return self.name