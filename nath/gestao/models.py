from django.db import models
from home.models import CustomBaseModel
from nath.settings import AUTH_USER_MODEL


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

class Projeto(CustomBaseModel):

    laboratorio_pk = models.ForeignKey('Laboratorio', on_delete=models.CASCADE, related_name='laboratorio_projeto')
    responsavel_pk = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='usuario_projeto')
    nome = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nome

class Especie(CustomBaseModel):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class MaterialBiologico(CustomBaseModel):
    
    created_by = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='usuario_materialbiologico', blank=True, null=False)
    
    projeto_pk = models.ForeignKey('Projeto', on_delete=models.CASCADE, related_name='projeto_materialbiologico', blank=False, null=False)  

    tipo_material_choices = [
        ('T', 'Tecido'),
        ('ST', 'Sangue Total'),
        ('S', 'Soro'),
        ('LH', 'Laminas Histológicas'),
        ('O', 'Outros')
        ]
    
    tipo_material = models.CharField(max_length=2, choices=tipo_material_choices, blank=False, null=False)
    especie = models.ForeignKey('Especie', on_delete=models.CASCADE, related_name='especie_materialbiologico')
    identificacao_interna_animal = models.CharField(max_length=100, blank=False, null=False)
    
    sexo_choices = [
        ('M', 'Masculino'),
        ('F', 'Feminino')
        ]
    
    sexo_animal = models.CharField(max_length=1, choices=sexo_choices, blank=True, null=True, verbose_name="Sexo do animal")
    data_coleta = models.DateField(blank=False, null=False, verbose_name="Data de Coleta do Material")
    meio_acondicionamento_choices = [
    ('R', 'RNA later'),
    ('F',  'Formaldeído'), 
    ('SM', 'Sem-Meio'),
    ('D', 'DMEN')
    ]
    meio_acondicionamento = models.CharField(max_length=2, choices=meio_acondicionamento_choices, blank=False, null=False)
    local_amostra = models.CharField(max_length=100, blank=False, null=False, verbose_name="Local da amostra")
    
    condicao_armazenamento_choices = [
        ('-80', '-80ºC'),
        ('-20', '-20ºC'),
        ('5~8', '5~8ºC'),
        ('TA', 'Temperatura Ambiente')
        ]
    condicao_armazenamento = models.CharField(max_length=3, choices=condicao_armazenamento_choices, blank=False, null=False)
    is_compartilhavel = models.BooleanField(default=False, verbose_name="Compartilhável")
    
    def __str__(self):
        return self.nome