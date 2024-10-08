from django.http import HttpResponse
from django.views.generic import ListView, TemplateView

from questionario.views import BasePermissoesView

from questionario.models import Noticia, Slideshow, Documento
class MegaFormsIndexView(BasePermissoesView,TemplateView):
    template_name = "questionario/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        noticias = Noticia.objects.all().order_by('-id')[:3]

        links_uteis = Documento.objects.filter(tipo__nome='Link Externo', tipo__ativo=True, ativo=True).extra(select={'length':'Length(`questionario_documento`.`nome`)'}).order_by('length')
        links_cae = Documento.objects.filter(tipo__nome='Links CAE', tipo__ativo=True, ativo=True)

        # print(f'Query: {links_cae}')

        slideshow = Slideshow.objects.all()

        context['noticias'] = noticias
        context['slideshow'] = slideshow
        context['links_uteis'] = links_uteis
        context['links_cae'] = links_cae

        return context
