from django.db import models

from questionario.models import ItemQuestionario, OpcoesItemQuestionario

class ItemDependente(models.Model):
    id = models.BigAutoField(primary_key=True)

    perguntaChave = models.ForeignKey(ItemQuestionario, verbose_name='Pergunta Principal', related_name='perguntaChave', on_delete=models.PROTECT, null=False, blank=False)

    pergunta = models.ForeignKey(ItemQuestionario, verbose_name='Pergunta Secundária', related_name='pergunta', on_delete=models.PROTECT, null=False, blank=False)

    opcao = models.ForeignKey(OpcoesItemQuestionario, verbose_name='Opção', on_delete=models.PROTECT, null=False, blank=False)
    
    ativo = models.BooleanField(verbose_name=u'Ativo?', default=True, editable=False)

    class Meta:
        verbose_name = 'Item Dependente'
        verbose_name_plural = 'Itens Dependentes'
        ordering = ['id']

    def __str__(self):
        return f'{self.id} - {self.perguntaChave} - {self.opcao}'