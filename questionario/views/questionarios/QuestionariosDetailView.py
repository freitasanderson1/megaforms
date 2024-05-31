from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.db.models import Q

from questionario.forms import QuestionarioForm
from questionario.models import TipoQuestionario, ItemQuestionario, Respostas, QuemRespondeu

from questionario.views import BasePermissoesView

import numpy as np


class QuestionariosDetailView(BasePermissoesView, TemplateView):
    template_name = "questionario/questionarios/QuestionarioDetail.html"
    form = QuestionarioForm



    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        # print(f'Valor de Kwargs: {kwargs["slug"]}')
        slugQuestionario = kwargs["slug"]
        questionario = TipoQuestionario.objects.get(slug=slugQuestionario)

        context['questoes'] = ItemQuestionario.objects.filter(questionario=questionario)
        context['questionario'] = questionario
        context['form'] = self.form

        return context



    def dispatch(self, request, *args, **kwargs):
                
        form = QuestionarioForm()

        return super().dispatch(request, *args, **kwargs)