from questionario.views import BasePermissoesView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from questionario.models import TipoQuestionario, Respostas
class RelatoriosQuestionariosIndexView(LoginRequiredMixin,BasePermissoesView,ListView):
    template_name ='questionario/relatorios/indexRelatorios.html'
    queryset = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # respondidos = RespostasQuestionario.objects.all().order_by('questionario__id','escola')

        respondidos2 = Respostas.objects.all().order_by('questionario__id','-dataCadastro')

        slugs_questionario = list()

        # for resposta in respondidos:
        #     slugs_questionario.append(resposta.questionario.slug)
        
        for resposta in respondidos2:
            slugs_questionario.append(resposta.questionario.slug)

        slugs_questionario = list(set(slugs_questionario))

        questionario = TipoQuestionario.objects.filter(slug__in=slugs_questionario)

        context['respondidos'] = respondidos2

        context['questionario'] = questionario


        return context
