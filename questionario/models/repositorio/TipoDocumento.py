from django.db import models

CHOICE_TIPO =(
    (0, 'Documento'),
    (1, 'Link'),
)
class TipoDocumento(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(u'Nome', max_length=255)

    tipo = models.IntegerField(u'Tipos de Documento', default=0, choices=CHOICE_TIPO, null=False, blank=False)
    
    ativo = models.BooleanField(verbose_name=u'Ativo?', default=True, editable=True)

    class Meta:
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'Tipos de Documentos'
        ordering = ['id','nome']

    def __str__(self):
        return f'{self.nome}'
