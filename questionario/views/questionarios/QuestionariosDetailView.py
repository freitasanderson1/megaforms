from django.views.generic import TemplateView

from questionario.models import TipoQuestionario, QuemRespondeu
from questionario.views import BasePermissoesView

import numpy as np


class QuestionariosDetailView(BasePermissoesView, TemplateView):
    template_name = "questionario/questionarios/QuestionarioDetail.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        slugQuestionario = kwargs["slug"]
        questionario = TipoQuestionario.objects.get(slug=slugQuestionario)

        if questionario.tipoDoQuestionario == 1:
            qsIdsQuemRespondeu = list(set(questionario.respostas_set.all().values_list('questionario__id',flat=True)))
            qsQuemRespondeu = QuemRespondeu.objects.filter(id__in=qsIdsQuemRespondeu)
            
            context['quemRespondeu'] = qsQuemRespondeu

            print(f'Total: {qsQuemRespondeu}')
        context['questionario'] = questionario

        return context