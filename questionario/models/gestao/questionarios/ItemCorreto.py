from django.db import models

from questionario.models import ItemQuestionario

class ItemCorreto(models.Model):
    id = models.BigAutoField(primary_key=True)

    opcao = models.ForeignKey(ItemQuestionario, verbose_name='Opção Associativa', on_delete=models.PROTECT, null=False, blank=False)

    valor = models.BooleanField(u'Correto?',default=False)


    class Meta:
        verbose_name = 'Opção Correta'
        verbose_name_plural = 'Opções Corretas'
        ordering = ['id']
        unique_together = ['valor','opcao']

    def __str__(self):
        return f'{self.id} - {self.valor} - {self.opcao}'