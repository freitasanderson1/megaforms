from django.db import models
from django.contrib.auth.models import User

from questionario.models import TipoQuestionario, ItemQuestionario
from AGF.models.Escola import Escola

CHOICES_QUESTIONARIO =(
    (0, 'Não'),
    (1, 'Sim'),
    (2, 'Não se aplica')
)

class RespostasQuestionario(models.Model):
    id = models.BigAutoField(primary_key=True)

    escola = models.ForeignKey(Escola, verbose_name='Escola', on_delete=models.PROTECT, null=False, blank=False)
    questionario = models.ForeignKey(TipoQuestionario, verbose_name='Nome do Questionario', on_delete=models.PROTECT, null=False, blank=False)
    pergunta = models.ForeignKey(ItemQuestionario, verbose_name='Pergunta do Questionario', on_delete=models.PROTECT, null=False, blank=False)
    valor = models.IntegerField(u'Valores que podem ser selecionados', default=1, choices=CHOICES_QUESTIONARIO)
    quemCadastrou = models.ForeignKey(User, verbose_name='Quem Cadastrou', null=True, blank=True, default=None, on_delete=models.PROTECT)


    class Meta:
        verbose_name = 'Resposta de Questionário (Escolar)'
        verbose_name_plural = 'Respostas de Questionários (Escolar)'
        ordering = ['id']

    def __str__(self):
        return f'{self.id} - {self.escola} - {self.questionario.quemCadastrou}'