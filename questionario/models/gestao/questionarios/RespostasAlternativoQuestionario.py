from django.db import models
from django.contrib.auth.models import User

from questionario.models import TipoQuestionario, ItemQuestionario, QuemRespondeu

class RespostasAlternativoQuestionario(models.Model):
    id = models.BigAutoField(primary_key=True)

    questionario = models.ForeignKey(TipoQuestionario, verbose_name='Nome do Questionario', on_delete=models.PROTECT, null=False, blank=False)
    pergunta = models.ForeignKey(ItemQuestionario, verbose_name='Pergunta do Questionario', on_delete=models.PROTECT, null=False, blank=False)
    valor = models.TextField(u'Resposta', max_length=2800, null=False, blank=False)
    quemRespondeu = models.ForeignKey(QuemRespondeu, verbose_name='Quem Respondeu', null=True, blank=True, default=None, on_delete=models.PROTECT)
    dataCadastro = models.DateTimeField(u'Data de Cadastro', auto_now_add=True, blank =True)
    dataAlteracao = models.DateTimeField(u'Última Alteração', auto_now=True, blank=True)

    class Meta:
        verbose_name = 'Resposta Alternativo'
        verbose_name_plural = 'Respostas Alternativas'
        ordering = ['id']

    def __str__(self):
        return f'{self.id}-{self.quemRespondeu.cidade}-{self.quemRespondeu.cargo}-{self.quemRespondeu.nome}'