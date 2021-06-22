from django.db import models

# Create your models here.
class Tarefas(models.Model):

    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.titulo