from django.db import models

from questionario.models import ItemQuestionario

class ItemAssociativo(models.Model):
    id = models.BigAutoField(primary_key=True)

    opcao = models.ForeignKey(ItemQuestionario, verbose_name='Opção Associativa', on_delete=models.PROTECT, null=False, blank=False)

    valor = models.TextField(u'Resposta', max_length=5000, null=False, blank=False)


    class Meta:
        verbose_name = 'Opção Associativa'
        verbose_name_plural = 'Opções Associativas'
        ordering = ['id']
        unique_together = ['valor','opcao']

    def __str__(self):
        return f'{self.id} - {self.valor} - {self.opcao}'