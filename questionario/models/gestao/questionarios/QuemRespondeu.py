from django.db import models

SEXO_CHOICES =(
    (0, 'Feminino'),
    (1, 'Masculino'),
)

class QuemRespondeu(models.Model):
    id = models.BigAutoField(primary_key=True)

    nome = models.TextField(u'Nome', max_length=100, null=False, blank=False)
    sobrenome = models.TextField(u'Sobrenome', max_length=100, null=False, blank=False)
    
    telefone = models.CharField('Telefone', max_length=20, null=True, blank=True)
    email = models.EmailField(u'Email', max_length=100, null=True, blank=True)
    cidade = models.TextField(u'Cidade', max_length=100, null=True, blank=True)
    cargo = models.TextField(u'Ocupação', max_length=100, null=True, blank=True)
    
    idade = models.IntegerField('Idade de quando Respondeu', null=True, blank=True)
    sexo = models.IntegerField(u'Sexo', default=0, choices=SEXO_CHOICES, null=True, blank=True)


    ativo = models.BooleanField(verbose_name=u'Ativo?', default=True, editable=False)

    class Meta:
        verbose_name = 'Quem Respondeu'
        verbose_name_plural = 'Quem Respondeu'
        ordering = ['id','ativo']

    def __str__(self):
        retorno = f'Item {self.id} - {self.nome} {self.sobrenome}'

        if self.cargo:
            retorno += f' - {self.cargo}'

        if self.cidade:
            retorno += f'({self.cidade})'

        return retorno 
