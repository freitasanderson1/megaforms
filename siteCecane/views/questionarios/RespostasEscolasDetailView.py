from django.http import HttpResponse

from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from siteCecane.models import TipoQuestionario, ItemQuestionario, RespostasQuestionario

from siteCecane.views import BasePermissoesView

class RespostasEscolasDetailView(LoginRequiredMixin,BasePermissoesView,TemplateView):

    template_name = "siteCecane/questionarios/respostasEscolasDetail.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        escola_id = kwargs['pk']
        questionario_slug = kwargs['slug']

        context['escola_id'] = escola_id
        context['questionario_slug'] = questionario_slug

        if self.ehGestor or self.ehSuperUser:


            context['respondidos'] = RespostasQuestionario.objects.filter(escola__id=escola_id, questionario__slug=questionario_slug).order_by('questionario__id','escola')

        else:

            context['respondidos'] = RespostasQuestionario.objects.filter(quemCadastrou=self.request.user, escola__id=escola_id, questionario__slug=questionario_slug).order_by('questionario__id','escola')

        context['quemCadastrou'] = context['respondidos'].first().quemCadastrou.get_full_name()

        return context
