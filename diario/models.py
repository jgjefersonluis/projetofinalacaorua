from django.db import models

from django.contrib.auth.models import User
from django.db import models

class Diario(models.Model):
    data = models.DateField()
    hora = models.TimeField()
    local = models.CharField(max_length=200)
    profissional = models.CharField(max_length=50)
    acao = models.CharField(max_length=300)
    sujeitos = models.CharField(max_length=350)
    avaliacao = models.CharField(max_length=400)

    def __str__(self):
        return self.local