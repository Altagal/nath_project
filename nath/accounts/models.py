from datetime import datetime
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class MyAccountManager(BaseUserManager):
    def create_user(self, email, password=None, first_name=None, last_name=None):
        if not email:
            raise ValueError('Usuario deve preencher o campo email')
        if not first_name:
            raise ValueError('Usuario deve preencher o campo Nome')
        if not last_name:
            raise ValueError('Usuario deve preencher o campo Sobrenome')

        user = self.model(
            email=email,
            first_name=first_name.title(),  # torna maiusculo os nomes
            last_name=last_name.title()  # torna maiusculo os sobrenomes
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, first_name, last_name):
        user = self.create_user(email=email, password=password, first_name=first_name,
                                last_name=last_name)

        user.username = None
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.is_verified = True

        user.save(using=self._db)

        return user


class Account(AbstractUser, BaseUserManager):
    username = models.CharField(max_length=100, null=True,
                                blank=True)  # atributo nao usado, se possivel deixar em branco

    first_name = models.CharField(max_length=150, blank=True, verbose_name='Nome')
    last_name = models.CharField(max_length=150, blank=True, verbose_name='Sobrenome')
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, verbose_name='Senha')

    last_login = models.DateTimeField(default=datetime.now, verbose_name='Ultimo login')
    date_joined = models.DateTimeField(default=datetime.now, verbose_name='Data de criação')

    is_active = models.BooleanField(default=False, verbose_name='Ativo')  # ativação é feita só pelo superuser ou admin
    is_verified = models.BooleanField(default=False)  # verificação pelo email institucional

    # Campos nao ultilizados
    # is_staff = models.BooleanField(default=False)
    # is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']  # Add List of fields which you want to be required

    objects = MyAccountManager()

    class Meta:
        # todas as permissoes do sistema serão alocadas aqui
        permissions = [
        
            ('active_user', 'Ativar Usuário'),
            ('user_to_group', 'Atribuir Usuário a Grupo'),
            ('add_group', 'Cadastrar Grupo'),
            ('view_group', 'Ver Grupo'),
            ('change_group', 'Editar Grupo'),
            ('delete_group', 'Excluir Grupo'),
  
            ('add_projeto', 'Cadastrar Projeto'),
            ('view_projeto', 'Ver Projeto'),
            ('change_projeto', 'Editar Projeto'),
            ('delete_projeto', 'Excluir Projeto'),

            ('add_laboratorio', 'Cadastrar Laboratorio'),
            ('view_laboratorio', 'Ver Laboratorio'),
            ('change_laboratorio', 'Editar Laboratorio'),
            ('delete_laboratorio', 'Excluir Laboratorio'),

            ('add_especie', 'Cadastrar Especie'),
            ('view_especie',  'Ver Especie'),
            ('change_especie', 'Editar Especie'),
            ('delete_especie', 'Excluir Especie'),
        ]

    def __str__(self):
        return self.email

    def set_status(self, status):
        self.is_active = status
