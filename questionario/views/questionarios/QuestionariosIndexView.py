from typing import Any
from django import http
from django.http import HttpResponse
from django.http.response import HttpResponse

from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from questionario.models import TipoQuestionario, ItemQuestionario, Respostas

from questionario.views import BasePermissoesView

class QuestionariosIndexView(LoginRequiredMixin,BasePermissoesView,TemplateView):

    template_name = "questionario/questionarios/indexQuestionarios.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context['questionario'] = TipoQuestionario.objects.filter(ativo=True).order_by('nome')

        # print(f"Session: {self.request.session['idUserFake']}")
        respostas = Respostas.objects.filter(
            # questionario__quemCadastrou=self.request.session['idUserFake'], 
            questionario__ativo=True).values('questionario__nome','questionario__slug').distinct()

        r = list(respostas)
        r = {x['questionario__nome']:x for x in r}.values()
        
        context['questionariosRespondidos'] = r

        return context
