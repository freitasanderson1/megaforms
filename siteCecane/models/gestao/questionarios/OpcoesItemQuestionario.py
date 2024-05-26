from django.db import models

from siteCecane.models import ItemQuestionario

class OpcoesItemQuestionario(models.Model):
    id = models.BigAutoField(primary_key=True)

    pergunta = models.ForeignKey(ItemQuestionario, verbose_name='Pergunta do Questionario', on_delete=models.PROTECT, null=False, blank=False)

    valor = models.TextField(u'Resposta', max_length=100, null=False, blank=False)


    class Meta:
        verbose_name = 'Opção de Resposta'
        verbose_name_plural = 'Opções de Respostas'
        ordering = ['id']
        unique_together = ['valor','pergunta']

    def __str__(self):
        return f'{self.id} - {self.valor} - {self.pergunta}'