from django.http import HttpResponse
from django.db.models import Q
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from questionario.models import TipoQuestionario, ItemQuestionario, Respostas, QuemRespondeu, VinculoQuestionario

from questionario.views import BasePermissoesView

class RelatorioQuestionarioView(LoginRequiredMixin, BasePermissoesView, TemplateView):

    template_name = "questionario/questionarios/RelatorioDetail.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        
        if self.ehGestor or self.ehSuperUser:
            questionario = TipoQuestionario.objects.get(slug=kwargs['slug'])
            
            perguntas = ItemQuestionario.objects.filter(questionario=questionario,ativo=True)
            
            vinculo = VinculoQuestionario.objects.get(questionarioPre=questionario) if questionario.tipoDoQuestionario == 0 else VinculoQuestionario.objects.get(questionarioPos=questionario)

            quemRespondeu = list(set(Respostas.objects.filter(Q(questionario=vinculo.questionarioPre)|Q(questionario=vinculo.questionarioPos)).values_list('quemRespondeu',flat=True)))

            pessoas = QuemRespondeu.objects.filter(id__in=quemRespondeu).order_by('nome','sobrenome')

            print(f"Total: {len(list(set(Respostas.objects.filter(Q(questionario=vinculo.questionarioPre)|Q(questionario=vinculo.questionarioPos)).values_list('quemRespondeu',flat=True).distinct())))}")
            context['pessoas'] = pessoas
            context['slug'] = kwargs['slug']
            
        return context