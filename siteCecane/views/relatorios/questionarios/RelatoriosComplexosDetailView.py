from siteCecane.views import BasePermissoesView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from siteCecane.models import RespostasAlternativoQuestionario, TipoQuestionario, ItemQuestionario,QuemRespondeu
class Object(object):
    questao = ''
    respostasSim = 0
    respostasNao = 0
    respostasNSA = 0

class RelatoriosComplexosDetailView(LoginRequiredMixin,BasePermissoesView,TemplateView):
    template_name ='siteCecane/relatorios/relatoriosComplexosDetail.html'
    queryset = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        questionario_slug = kwargs.get('slug')

        perguntas = ItemQuestionario.objects.filter(questionario__slug=questionario_slug)

        respostas = RespostasAlternativoQuestionario.objects.filter(questionario__slug=questionario_slug)

        context['questionario'] = perguntas[0].questionario
        context['perguntas'] =  perguntas
        context['respostas'] = respostas

        relatorios = list()

        # print(f'Tamanho: {len(perguntas)}')


        # for pergunta in perguntas:

        #     questoes = Object()
        #     questoes.questao = f'{pergunta.descricao}'
        #     questoes.respostasSim = len(RespostasQuestionario.objects.filter(questionario=questionario,pergunta=pergunta,valor=1))
        #     questoes.respostasNao = len(RespostasQuestionario.objects.filter(questionario=questionario,pergunta=pergunta,valor=0))
        #     questoes.respostasNSA = len(RespostasQuestionario.objects.filter(questionario=questionario,pergunta=pergunta,valor=2))
        
        #     relatorios.append(questoes)




        context['relatorios'] = relatorios

        return context
