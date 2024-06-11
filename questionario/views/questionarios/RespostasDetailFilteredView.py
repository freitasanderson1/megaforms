from django.http import HttpResponse

from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from questionario.models import TipoQuestionario, ItemQuestionario, Respostas, QuemRespondeu

from questionario.views import BasePermissoesView

class RespostasDetailFilteredView(BasePermissoesView, TemplateView):
    
    template_name = "questionario/questionarios/RespostasDetail.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        slug = kwargs['slug']

        if self.ehGestor or self.ehSuperUser:

            questionario = TipoQuestionario.objects.get(slug=slug)
            perguntas = ItemQuestionario.objects.filter(questionario=questionario,ativo=True)
            
            # print(f'Questionário: {questionario}')
            
            cidades = list()
            totalPessoas = list()

            respostas = Respostas.objects.filter(questionario=questionario).order_by('id')
            
            for resposta in respostas:
                cidades.append(resposta.quemRespondeu.cidade)
                totalPessoas.append(resposta.quemRespondeu.id)


            cidades = sorted(list(set(cidades)))
            totalPessoas = list(set(totalPessoas))
            excluirPessoas = []
            pessoas = QuemRespondeu.objects.filter(id__in=totalPessoas).order_by('nome')

            for pessoa in pessoas:
                for pergunta in perguntas:
                    existeResposta = respostas.filter(~Q(valor=''),pergunta__tipo__in=[0,1,3],pergunta=pergunta,quemRespondeu=pessoa).exists()

                    # print(f'Resposta: {existeResposta}')
                    if not existeResposta:
                        excluirPessoas.append(pessoa.id)

            objPessoas = list()
            
            # print(f'Total: {len(excluirPessoas)} - {cidades}')

            for cidade in cidades:
                listaDados = list()

                for pessoa in pessoas:
                    
                    if pessoa.cidade == cidade and pessoa.id not in excluirPessoas:
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

            # print(f'Pessoas: {len(objPessoas[0]["dados"])}')

            context['questionario'] = questionario
            context['totalPessoas'] = pessoas.count()
            context['pessoas'] = objPessoas
            context['cidades'] = cidades

        return context