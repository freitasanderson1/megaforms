from django.http import HttpResponse

from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from siteCecane.models import TipoQuestionario, ItemQuestionario, RespostasQuestionario

from siteCecane.views import BasePermissoesView

class RespostasEscolasIndexView(LoginRequiredMixin, BasePermissoesView, TemplateView):

    template_name = "siteCecane/questionarios/respostasEscolas.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        questionarioRespondido_slug = kwargs['slug']

        context['questionarioRespondido'] = TipoQuestionario.objects.get(slug=questionarioRespondido_slug)
        context['questionarioRespondido_id'] = questionarioRespondido_slug
        if self.ehGestor or self.ehSuperUser:

            respostasQuestionario = RespostasQuestionario.objects.filter(questionario__slug=questionarioRespondido_slug).order_by('questionario__id','escola')

        else:

            respostasQuestionario = RespostasQuestionario.objects.filter(quemCadastrou=self.request.user, questionario__slug=questionarioRespondido_slug).order_by('questionario__id','escola')

        context['respondidos'] = respostasQuestionario

        context['escolas'] = []
        for resposta in respostasQuestionario:

            context['escolas'].append(resposta.escola)

        context['escolas'] = list(set(context['escolas']))
        return context
