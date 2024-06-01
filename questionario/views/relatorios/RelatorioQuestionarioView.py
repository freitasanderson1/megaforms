from django.http import HttpResponse

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from questionario.models import TipoQuestionario, ItemQuestionario, Respostas, QuemRespondeu

from questionario.views import BasePermissoesView

class RelatorioQuestionarioView(LoginRequiredMixin, BasePermissoesView, TemplateView):

    template_name = "questionario/questionarios/RelatorioDetail.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        if self.ehGestor or self.ehSuperUser:

            context['slug'] = kwargs['slug']
            
        return context