from django.db import models

class QuemRespondeu(models.Model):
    id = models.BigAutoField(primary_key=True)

    nome = models.TextField(u'Nome', max_length=100, null=False, blank=False)
    sobrenome = models.TextField(u'Sobrenome', max_length=100, null=False, blank=False)
    
    telefone = models.CharField('Telefone', max_length=20, null=False, blank=False)
    email = models.EmailField(u'Email', max_length=100, null=False, blank=False)
    cidade = models.TextField(u'Cidade', max_length=100, null=False, blank=False)
    cargo = models.TextField(u'Cargo', max_length=100, null=False, blank=False)
    
    dataAniversario = models.DateField('Data de Aniversário', null=True, blank=True)

    ativo = models.BooleanField(verbose_name=u'Ativo?', default=True, editable=False)

    class Meta:
        verbose_name = 'Quem Respondeu'
        verbose_name_plural = 'Quem Respondeu'
        ordering = ['id','ativo']

    def __str__(self):
        return f'Item {self.id} - {self.nome} {self.sobrenome} - {self.cargo} ({self.cidade})'
