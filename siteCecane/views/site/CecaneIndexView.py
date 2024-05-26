from django.http import HttpResponse
from django.views.generic import ListView, TemplateView

from siteCecane.views import BasePermissoesView

from siteCecane.models import Noticia, Slideshow, Documento
class CecaneIndexView(BasePermissoesView,TemplateView):
    template_name = "siteCecane/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        noticias = Noticia.objects.all().order_by('-id')[:3]

        links_uteis = Documento.objects.filter(tipo__nome='Link Externo', tipo__ativo=True, ativo=True).extra(select={'length':'Length(`siteCecane_documento`.`nome`)'}).order_by('length')
        links_cae = Documento.objects.filter(tipo__nome='Links CAE', tipo__ativo=True, ativo=True)

        # print(f'Query: {links_cae}')

        slideshow = Slideshow.objects.all()

        context['noticias'] = noticias
        context['slideshow'] = slideshow
        context['links_uteis'] = links_uteis
        context['links_cae'] = links_cae

        return context
