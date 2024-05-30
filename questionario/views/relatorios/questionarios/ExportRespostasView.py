from questionario.views import BasePermissoesView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from questionario.models import RespostasAlternativoQuestionario, TipoQuestionario, ItemQuestionario,QuemRespondeu

import pandas as pd

class ExportRespostasView(LoginRequiredMixin,BasePermissoesView,TemplateView):
    template_name ='questionario/relatorios/relatoriosComplexosDetail.html'
    queryset = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        objQuestionario = TipoQuestionario.objects.get(slug=kwargs.get('slug'))

        relatorio = dict()

        relatorio['nome'] = list()
        relatorio['telefone'] = list()
        relatorio['email'] = list()
        relatorio['cidade'] = list()
        relatorio['cargo'] = list()
        relatorio['dataAniversario'] = list()

        perguntas = ItemQuestionario.objects.filter(questionario=objQuestionario,ativo=True)

        pessoas = RespostasAlternativoQuestionario.objects.filter(questionario=objQuestionario).values('quemRespondeu')

        listPessoas = list()
        [listPessoas.append(pessoa.get('quemRespondeu')) for pessoa in pessoas]

        listPessoas = list(set(listPessoas))
        
        for item in perguntas:
            relatorio[str(item.descricao).strip()]= list()

        # print(f'Total Perguntas {relatorio}')
        # for index,item in enumerate(relatorio):
        #     print(f'{index} - {item}\n')

        # print(f'Total Pessoas: {len(listPessoas)}')

        for pessoaId in listPessoas:
            pessoa = QuemRespondeu.objects.get(id=pessoaId)
            # print(f'Pessoa: {pessoa} - {pessoa.dataAniversario}\n')
            respostas = pessoa.respostasalternativoquestionario_set.all()

            relatorio['nome'].append(f'{pessoa.nome} {pessoa.sobrenome}')
            relatorio['telefone'].append(pessoa.telefone.strip())
            relatorio['email'].append(pessoa.email.strip())
            relatorio['cidade'].append(pessoa.cidade.strip())
            relatorio['cargo'].append(pessoa.cargo.strip())
            relatorio['dataAniversario'].append(pessoa.dataAniversario.strftime('%d/%m/%Y')) if pessoa.dataAniversario else  relatorio['dataAniversario'].append(' ')

            # print(f'{len(relatorio.get("dataAniversario"))}')

            # print(f'Tamanho: {len(respostas)}')

            for resposta in respostas:
                # if not resposta.valor:
                #     print(f'Pergunta: {str(resposta.pergunta.descricao).strip()}\n')

                #     print(f'Resposta: {resposta.valor.strip()}\n')
                relatorio[str(resposta.pergunta.descricao).strip()].append(resposta.valor.strip().replace('\r\n',',')) if resposta.valor else relatorio[str(resposta.pergunta.descricao).strip()].append('')

        # for item in relatorio:
        #     print(f'Tam: {len(relatorio[item])}')

        dados = pd.DataFrame(data=relatorio)

        # print(f'Dados: {dados}')
        dados.to_csv(f'{objQuestionario.nome}.csv', index=False)
        
        return context