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
            
            vinculo = VinculoQuestionario.objects.get(questionarioPre=questionario) if questionario.tipoDoQuestionario == 0 else VinculoQuestionario.objects.get(questionarioPos=questionario)

            quemRespondeuPre = list(set(Respostas.objects.filter(questionario=vinculo.questionarioPre).values_list('quemRespondeu',flat=True)))
            quemRespondeuPos = list(set(Respostas.objects.filter(questionario=vinculo.questionarioPos).values_list('quemRespondeu',flat=True)))


            pessoas = QuemRespondeu.objects.filter(Q(id__in=quemRespondeuPre)&Q(id__in=quemRespondeuPos)).order_by('nome','sobrenome')

            print(f"Total: {len(pessoas)}")

            context['pessoas'] = pessoas
            context['slug'] = kwargs['slug']
            
        return context