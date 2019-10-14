from django.db import models


# Create your models here.
class Moeda(models.Model):
    nome = models.CharField(max_length=30)
    preco = models.IntegerField()
    dt_criacao = models.DateField()
