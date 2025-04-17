from django.db import models
from home.models import CustomBaseModel

class Laboratorio(CustomBaseModel):

    nome = models.CharField(max_length=100, unique=True)
    endereco = models.CharField(max_length=255)
    instituicao = models.CharField(max_length=100, default="Fiocruz")
    email = models.EmailField(max_length=100, unique=True)
    
    padrao_sanitario_choices = [
        ('NB1', 'NB1'),
        ('NB2', 'NB2'),
        ('NB3', 'NB3'),
    ]

    padrao_sanitario = models.CharField(max_length=3, choices=padrao_sanitario_choices, blank=False, null=False)

    def __str__(self):
        return self.nome