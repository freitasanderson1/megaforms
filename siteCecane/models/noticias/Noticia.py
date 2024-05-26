from django.db import models


class Noticia(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.TextField(u'Título da Notícia:', max_length=255)
    img = models.ImageField(u'Imagem da Notícia', upload_to='noticias',null=True, blank=True)
    subtitulo = models.TextField(u'Subtítulo da Notícia', max_length=280, null=True, blank=True)
    noticia = models.TextField(u'Corpo da Notícia',)
    ativo = models.BooleanField(verbose_name=u'Ativo?', default=True, editable=False)
    dataCadastro = models.DateTimeField(u'Data de Cadastro', auto_now_add=True, blank =True)
    dataAlteracao = models.DateTimeField(u'Última Alteração', auto_now=True, blank=True)


    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'
        ordering = ['id']

    def __str__(self):
        return f'Noticia: {self.id} - {self.titulo}'
