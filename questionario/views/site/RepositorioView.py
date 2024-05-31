from django.http import HttpResponse
from django.views.generic import ListView, TemplateView

from questionario.views import BasePermissoesView

from questionario.models import Documento, TipoDocumento

class RepositorioView(BasePermissoesView,TemplateView):
    template_name = "questionario/repositorio.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        tipos = TipoDocumento.objects.filter(ativo=True)

        for tipo in tipos:
            tipo.documentos = tipo.documento_set.filter(ativo=True)

        context['tipos'] = tipos
        
        return context
