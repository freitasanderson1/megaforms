from django.db import models
from django.contrib.auth.models import User

from questionario.models import TipoQuestionario, ItemQuestionario, QuemRespondeu
from AGF.models.Escola import Escola

class Respostas(models.Model):
    id = models.BigAutoField(primary_key=True)
    
    questionario = models.ForeignKey(TipoQuestionario, verbose_name='Nome do Questionario', on_delete=models.PROTECT, null=False, blank=False)

    ## Somente para escolares
    escola = models.ForeignKey(Escola, verbose_name='Escola', on_delete=models.PROTECT, null=False, blank=False)
    quemCadastrou = models.ForeignKey(User, verbose_name='Quem Cadastrou', null=True, blank=True, default=None, on_delete=models.PROTECT)
    #############
    
    ###Somente para Outros Tipos
    quemRespondeu = models.ForeignKey(QuemRespondeu, verbose_name='Quem Respondeu', null=True, blank=True, default=None, on_delete=models.PROTECT)
    #################

    pergunta = models.ForeignKey(ItemQuestionario, verbose_name='Pergunta do Questionario', on_delete=models.PROTECT, null=False, blank=False)
    
    valor = models.TextField(u'Resposta', max_length=100, null=False, blank=False)
    dataCadastro = models.DateTimeField(u'Data de Cadastro', auto_now_add=True, blank =True)
    dataAlteracao = models.DateTimeField(u'Última Alteração', auto_now=True, blank=True)
    
    ativo = models.BooleanField(verbose_name=u'Ativo?', default=True, editable=False)



    class Meta:
        verbose_name = 'Resposta de Questionário'
        verbose_name_plural = 'Respostas de Questionários'
        ordering = ['id']

    def __str__(self):
        retorno = f'{self.id} - {self.escola} - {self.quemCadastrou}' if self.escola else f'{self.id}-{self.quemRespondeu.cidade}-{self.quemRespondeu.cargo}-{self.quemRespondeu.nome}'
        return retorno