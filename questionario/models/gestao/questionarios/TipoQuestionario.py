from django.db import models
from django.contrib.auth.models import User
from slugify import slugify

TIPO_QUESTIONARIO =(
    (0, 'Escolar'),
    (1, 'CAE'),
    (2, 'Agricultores'),
    (3, 'Gestão AF')
)

class TipoQuestionario(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.TextField(u'Nome do Questionário:', max_length=255)
    descricao = models.TextField(u'Descrição do Questionário', max_length=280, null=True, blank=True)
    tipoDoQuestionario = models.IntegerField(u'Tipos de questionário', default=0, choices=TIPO_QUESTIONARIO, null=True, blank=True)
    slug = models.SlugField('Slug', max_length=150, unique=True, blank=True, null=False)
    ativo = models.BooleanField(verbose_name=u'Ativo?', default=True, editable=True)

    quemCadastrou = models.ForeignKey(User, verbose_name='Quem Cadastrou', null=True, blank=True, default=None, on_delete=models.PROTECT)
    dataCadastro = models.DateTimeField(u'Data de Cadastro', auto_now_add=True, blank =True)
    dataAlteracao = models.DateTimeField(u'Última Alteração', auto_now=True, blank=True)


    class Meta:
        verbose_name = 'Questionário'
        verbose_name_plural = 'Questionários'
        ordering = ['id','nome','dataCadastro']

    def __str__(self):
        return f'{self.id} - {self.nome}'

    def save(self, *args, **kwargs):
        if not self.slug:

            self.slug = slugify(self.nome)

            slug2=  TipoQuestionario.objects.filter(slug__contains = self.slug)

            print(f'Quantos Questionários já existem com este nome: {len(slug2)+1}')
            if slug2:
                import datetime

                today = datetime.date.today()

                self.slug += (f'{today.year}')

            print(f'O Slug ficou assim: {self.slug}')

        super(TipoQuestionario, self).save()
