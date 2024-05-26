from django.http import HttpResponse
from django.views.generic import ListView, TemplateView

from siteCecane.views import BasePermissoesView

class PoliticaPrivacidadeView(BasePermissoesView,TemplateView):
    template_name = "siteCecane/privacidade.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        return context
