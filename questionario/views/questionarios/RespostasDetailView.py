from django.http import HttpResponse

from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from questionario.models import TipoQuestionario, ItemQuestionario, Respostas, QuemRespondeu

from questionario.views import BasePermissoesView

class RespostasDetailView(LoginRequiredMixin, BasePermissoesView, TemplateView):

    template_name = "questionario/questionarios/RespostasDetail.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        slug = kwargs['slug']

        if self.ehGestor or self.ehSuperUser:

            questionario = TipoQuestionario.objects.get(slug=slug)

            print(f'Questionário: {questionario}')
            
            cidades = list()
            totalPessoas = list()

            respostas = Respostas.objects.filter(questionario=questionario).order_by('id')

            for resposta in respostas:
                cidades.append(resposta.quemRespondeu.cidade)
                totalPessoas.append(resposta.quemRespondeu.id)

            cidades = sorted(list(set(cidades)))
            totalPessoas = list(set(totalPessoas))

            pessoas = QuemRespondeu.objects.filter(id__in=totalPessoas).order_by('nome')

            objPessoas = list()

            for cidade in cidades:
                listaDados = list()

                for pessoa in pessoas:
                    
                    if pessoa.cidade == cidade:
                        respostasDaPessoa = Respostas.objects.filter(questionario=questionario,quemRespondeu=pessoa)
                        dados = {
                            'pessoa': pessoa,
                            'respostas': respostasDaPessoa
                        }
                        listaDados.append(dados)

                dictPessoa = {
                    'cidade': cidade,
                    'dados': listaDados,
                }

                objPessoas.append(dictPessoa)

            # for pessoa in pessoas:
            #     print(pessoa,'\n')

            # for cidade in cidades:

            #     print(cidade,'\n')
           
            context['questionario'] = questionario

            context['pessoas'] = objPessoas
            context['cidades'] = cidades

        return context