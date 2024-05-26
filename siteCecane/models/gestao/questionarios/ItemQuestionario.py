from django.db import models
from siteCecane.models import TipoQuestionario

TIPO_QUESTÃO =(
    (0, 'Escolha'),
    (1, 'Multipla Escolha'),
    (2, 'Texto'),
)

class ItemQuestionario(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipo = models.IntegerField(u'Tipos de questão', default=0, choices=TIPO_QUESTÃO, null=True, blank=True)
    questionario = models.ForeignKey(TipoQuestionario, verbose_name='Nome do Questionario', on_delete=models.PROTECT, null=False, blank=False)
    descricao = models.TextField(u'Descrição do Item do Questionário', max_length=2000, null=True, blank=True)
    ativo = models.BooleanField(verbose_name=u'Ativo?', default=True, editable=False)

    class Meta:
        verbose_name = 'Item do Questionário'
        verbose_name_plural = 'Itens do Questionário'
        ordering = ['id','ativo']

    def __str__(self):
        return f'Item {self.id} - {self.descricao} - {self.tipo}'
