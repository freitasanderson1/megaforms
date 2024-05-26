from django.contrib.auth.models import User
from django.db import models

OPCAO_SEXO = (
		(None,'Ainda não verificado'),
		('M', 'Masculino'),
		######### OUTROS
		('F', 'Feminino'),
	)

class Pessoa(models.Model):
    user = models.OneToOneField(User, verbose_name=u'Usuário', null=False, unique=True, on_delete=models.CASCADE)

    nomeCompleto= models.CharField(verbose_name=u'Nome Completo',max_length=255)
    cpf = models.CharField('CPF', max_length=11, null=False, unique=True)
    email = models.CharField(u'Email principal', max_length=255,null=True, unique=True)
    contato = models.CharField('Fone de contato',max_length=255, null=True, blank=True, help_text='Fone de contato com DDD (63) 98765-4321', default=None)

    ativo = models.BooleanField(verbose_name=u'Ativo?',default=True, editable=True)

    sexo = models.CharField(u'Sexo', max_length=2, null=True, blank=True, choices=OPCAO_SEXO)
    
    dataNascimento = models.DateField('Data de Nascimento', null=True, blank=True)


    dataCadastro = models.DateTimeField('Data de Cadastro', auto_now_add=True, null=True)
    dataUltimaAlteracao = models.DateTimeField('Última alteração', null=True, blank=True, auto_now=True)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering = ['nomeCompleto','ativo']

    def __str__(self):
        return f'{self.nomeCompleto}'