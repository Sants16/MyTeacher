from lib2to3.refactor import MultiprocessingUnsupported
from pydoc import describe
from statistics import mode
from unicodedata import decimal
from django.db import models
from django.forms import CharField

# Create your models here.

class Professor(models.Model):
    # define o tamanho máximo de caracteres, o valor não pode ser nulo, não pode ser um valor em branco
    nome = models.CharField(
        max_length = 100, 
        null = False, 
        blank = False
    )
    valor_hora = models.DecimalField(
        max_digits = 9, 
        decimal_places = 2, 
        null = False, 
        blank = False
    )
    descricao = models.TextField(
        null = False, 
        blank = False
    )
    foto = models.URLField(
        max_length = 255, 
        null = False, 
        blank = False
    )

class Aula(models.Model):
    nome = models.CharField(
        max_length = 100,
        null = False,
        blank = False
    )
    email = models.EmailField(
        max_length = 255,
        null = False,
        blank = False
    )
    professor = models.ForeignKey(  # relacionando com o model Professor
        to = Professor, 
        on_delete = models.CASCADE, # on_delete, o que tem que acontecer quando o dado que estou me relacionando for apagado, ou seja quando o professor for apagado o que deve acontecer com as aulas, models.CASCADE = se apagar o professor também apaga as aulas
        related_name = 'aulas', # related_name, como eu posso conseguir encontrar as aulas atraves do professor, professor.aulas aparece as aulas do professor
        null = False, 
        blank = False
    )