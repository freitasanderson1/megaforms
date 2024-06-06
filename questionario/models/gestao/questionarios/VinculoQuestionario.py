from django.db import models
from questionario.models import TipoQuestionario

class VinculoQuestionario(models.Model):
    id = models.BigAutoField(primary_key=True)

    questionarioPre = models.ForeignKey(TipoQuestionario, verbose_name='Nome do Questionario', related_name='questionarioPre', on_delete=models.PROTECT, null=False, blank=False)
    questionarioPos = models.ForeignKey(TipoQuestionario, verbose_name='Nome do Questionario', related_name='questionarioPos', on_delete=models.PROTECT, null=False, blank=False)

    ativo = models.BooleanField(verbose_name=u'Ativo?', default=True, editable=False)

    class Meta:
        verbose_name = 'Vínculo do Questionário'
        verbose_name_plural = 'Vínculos dos Questionários'
        ordering = ['id','ativo']

    def __str__(self):
        return f'Vínculo {self.id} - {self.questionarioPre} <-> {self.questionarioPos}'
