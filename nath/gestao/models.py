from django.db import models
from home.models import CustomBaseModel
from nath.settings import AUTH_USER_MODEL  


class Laboratorio(CustomBaseModel):

    nome = models.CharField(max_length=100, unique=True)
    instituicao = models.CharField(max_length=100, default="Fiocruz", verbose_name="Instituição")
    email = models.EmailField(max_length=100, unique=True, verbose_name="E-mail de contato")
    padrao_sanitario_choices = [
        ('NB1', 'NB1'),
        ('NB2', 'NB2'),
        ('NB3', 'NB3'),
    ]

    padrao_sanitario = models.CharField(max_length=3, choices=padrao_sanitario_choices,  verbose_name="Padrão sanitário")

    
    def __str__(self):
        return self.nome

class EnderecoLaboratorio(CustomBaseModel):
    laboratorio_pk = models.ForeignKey('Laboratorio', on_delete=models.CASCADE, related_name='laboratorio_endereco')
    cep = models.CharField('CEP', max_length=9)
    logradouro = models.CharField('Logradouro', max_length=255)
    numero = models.CharField('Número', max_length=10)
    complemento = models.CharField('Complemento', max_length=255, blank=True, null=True)
    bairro = models.CharField('Bairro', max_length=100)
    cidade = models.CharField('Cidade', max_length=100)
    estado = models.CharField('Estado', max_length=2)
    pais = models.CharField('País', max_length=100, default='Brasil')


class Projeto(CustomBaseModel):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome do projeto")
    laboratorio_pk = models.ForeignKey('Laboratorio', on_delete=models.CASCADE, related_name='laboratorio_projeto', verbose_name="Laboratório")
    responsavel_pk = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='usuario_projeto', verbose_name="Responsável") 
    
    
    def __str__(self):
        return self.nome

class Especie(CustomBaseModel):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Amostra(CustomBaseModel):
    
    created_by = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='usuario_Amostra', blank=True, null=False)
    
    projeto_pk = models.ForeignKey('Projeto', on_delete=models.CASCADE, related_name='projeto_Amostra', blank=False, null=False)  


    tipo_amostra_choices = [
        ('T', 'Tecido'),
        ('ST', 'Sangue Total'),
        ('S', 'Soro'),
        ('LH', 'Laminas Histológicas'),
        ('P', 'Plasma'),
        ('O', 'Outros')
        ]
    tipo_amostra = models.CharField(max_length=2, choices=tipo_amostra_choices,  verbose_name="Tipo da amostra")
    data_coleta = models.DateField( verbose_name="Data da coleta da amotra", blank=False, null=False)
    meio_acondicionamento_choices = [
    ('R', 'RNA later'),
    ('RT', 'RNA later + Trizol'),
    ('T', 'Trizol'),
    ('F',  'Formaldeído'), 
    ('SM', 'Sem-Meio'),
    ('D', 'DMEN')
    ]
    meio_acondicionamento = models.CharField(max_length=2, choices=meio_acondicionamento_choices,  verbose_name="Meio de acondicionamento")
    condicao_armazenamento_choices = [
        ('-80', '-80ºC'),
        ('-20', '-20ºC'),
        ('5~8', '5~8ºC'),
        ('TA', 'Temperatura Ambiente')
        ]
    condicao_armazenamento = models.CharField(max_length=3, choices=condicao_armazenamento_choices,  verbose_name="Condição de armazenamento")
    especie = models.ForeignKey('Especie', on_delete=models.CASCADE, related_name='especie_Amostra', verbose_name="Espécie")
    sexo_choices = [
        ('M', 'Masculino'),
        ('F', 'Feminino')
        ]
    sexo_animal = models.CharField(max_length=1, choices=sexo_choices, blank=True, null=True, verbose_name="Sexo do animal")
    
    identificacao_interna_animal = models.CharField(max_length=100, blank=True, null=True, verbose_name="Identificação interna do animal")
    local_amostra = models.CharField(max_length=100, blank=True, null=True, verbose_name="Local da amostra")
    
    is_compartilhavel = models.BooleanField(default=False)
    
    
class SolicitacaoAmostra(CustomBaseModel):
    amostra_pk = models.ForeignKey('Amostra', on_delete=models.CASCADE, related_name='solicitacoes')
    usuario_solicitante_pk = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='usuario_solicitante')
    status_choices = [
        ('P', 'Pendente'),         
        ('A', 'Aceita'),
        ('R', 'Recusada'),
        ('E', 'Entregue'),
        ('C', 'Cancelada'),
        ]
    status = models.CharField(max_length=2, choices=status_choices,  default='P')