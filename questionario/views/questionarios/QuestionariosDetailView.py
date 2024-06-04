from django.views.generic import TemplateView

from questionario.models import TipoQuestionario
from questionario.views import BasePermissoesView

import numpy as np


class QuestionariosDetailView(BasePermissoesView, TemplateView):
    template_name = "questionario/questionarios/QuestionarioDetail.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        slugQuestionario = kwargs["slug"]
        questionario = TipoQuestionario.objects.get(slug=slugQuestionario)

        context['questionario'] = questionario

        return context