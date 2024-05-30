from django.http import HttpResponse
from django.views.generic import ListView, TemplateView

from questionario.views import BasePermissoesView

from questionario.models import Documento, TipoDocumento

class RepositorioView(BasePermissoesView,TemplateView):
    template_name = "questionario/repositorio.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        documentos = Documento.objects.filter(tipo__ativo=True, ativo=True).exclude(tipo__nome='Links CAE').exclude(tipo__nome='Link Externo')

        # print(f'Query: {documentos}')
        tipos = TipoDocumento.objects.filter(tipo=0, ativo=True).exclude(nome="Resoluções").exclude(nome="Modelos de Documentos")

        for tipo in tipos:
            tipo.documentos = tipo.documento_set.filter(ativo=True)

        context['tipos'] = tipos

        context['resolucoes'] = documentos.filter(tipo__nome="Resoluções")
        context['documentosEditaveis'] = documentos.filter(tipo__nome="Modelos de Documentos")


        return context
