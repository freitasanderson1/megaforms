from django.db import models

from cadastro.models import Pessoa
from questionario.models import TipoDocumento

import uuid


class Documento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    nome = models.CharField(u'Nome do Documento:', max_length=255)
    descricao = models.TextField(u'Descrição do Documento', max_length=500, null=True, blank=True)

    tipo = models.ForeignKey(TipoDocumento, verbose_name='Tipo do Documento', help_text="Guias, Cartilhas, Manuais, Gestão AF", on_delete=models.PROTECT,)

    arquivo = models.FileField(u'Arquivo', upload_to='repositorio/', null=True, blank=True)
    
    quemCadastrou = models.ForeignKey(Pessoa, verbose_name='Quem Cadastrou', null=True, blank=True, default=None, on_delete=models.PROTECT)

    dataCadastro = models.DateTimeField(u'Data de Cadastro', auto_now_add=True, blank =True)
    dataAlteracao = models.DateTimeField(u'Última Alteração', auto_now=True, blank=True)

    ativo = models.BooleanField(verbose_name=u'Ativo?', default=True, editable=True)

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
        ordering = ['dataCadastro','nome']

    def __str__(self):
        return f'{self.nome} - {self.tipo} ({self.dataCadastro})'
