from django.views.generic import TemplateView

from questionario.models import TipoQuestionario, QuemRespondeu, VinculoQuestionario
from questionario.views import BasePermissoesView

class QuestionariosDetailView(BasePermissoesView, TemplateView):
    template_name = "questionario/questionarios/QuestionarioDetail.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        slugQuestionario = kwargs["slug"]
        questionario = TipoQuestionario.objects.get(slug=slugQuestionario)

        if questionario.tipoDoQuestionario == 1:
            vinculo = VinculoQuestionario.objects.filter(questionarioPos=questionario).last()

            # print(f"Vinculo: {vinculo.questionarioPre.respostas_set.all().values_list('quemRespondeu__id',flat=True)}")

            qsIdsQuemRespondeuPre = list(set(vinculo.questionarioPre.respostas_set.all().values_list('quemRespondeu__id',flat=True)))
            qsIdsQuemRespondeuPos = list(set(vinculo.questionarioPos.respostas_set.all().values_list('quemRespondeu__id',flat=True)))

            qsQuemRespondeu = QuemRespondeu.objects.filter(id__in=qsIdsQuemRespondeuPre).exclude(id__in=qsIdsQuemRespondeuPos).order_by('nome')
            
            context['quemRespondeu'] = qsQuemRespondeu

            # print(f'Total: {qsQuemRespondeu}')
        context['questionario'] = questionario

        return context
