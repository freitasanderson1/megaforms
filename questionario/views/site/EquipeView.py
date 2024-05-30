from django.http import HttpResponse
from django.views.generic import ListView, TemplateView

from questionario.views import BasePermissoesView

class EquipeView(BasePermissoesView,TemplateView):
    template_name = "questionario/equipe.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        return context
