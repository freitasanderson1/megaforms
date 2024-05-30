from django.db import models

class Slideshow(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.TextField(u'Título do Slide', max_length=255)
    subtitulo = models.TextField(u'Subtítulo do Slide', max_length=280, null=True, blank=True)
    img = models.ImageField(u'Imagem do Slide',upload_to='slideshow')  
    ativo = models.BooleanField(verbose_name=u'Ativo?', default=True, editable=False)
    


    class Meta:
        verbose_name = 'Slideshow'
        verbose_name_plural = 'Slideshow'
        ordering = ['id']

    def __str__(self):
        return f'Slide número: {self.id}'