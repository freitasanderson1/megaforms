from django.http import JsonResponse
from django.shortcuts import redirect
from django.views import View
from django.contrib import messages

import numpy as np

from questionario.models import TipoQuestionario, QuemRespondeu, ItemQuestionario, Respostas

class QuestionarioRestView(View):

    def post(self, request, *args, **kwargs):
        print(f'Request: {request.POST}')
        # print(f'Kwargs: {kwargs}')
        
        data = request.POST

        questionario = TipoQuestionario.objects.get(id=kwargs.get('id'))

        if data.get('tipoQuestionario') == '0':
            quem = QuemRespondeu()

            nomeCompleto = data.get("nome").split(' ')
            nome, sobrenome = np.array_split(nomeCompleto, 2)

            quem.nome = str(nome).replace("'","").replace('[','').replace(']','')
            quem.sobrenome = str(sobrenome).replace("'","").replace('[','').replace(']','')
            quem.telefone = data.get("telefone")
            quem.email = data.get("email")
            quem.cidade = data.get("cidade")
            quem.cargo = data.get("cargo")
            quem.idade = data.get('idade', 0)
            quem.sexo = data.get('selectSexo')
            quem.vinculo = data.get('selectVinculo')

            quem.save()
        
        else:
            quem = QuemRespondeu.objects.get(id=data.get('selectCabecalho'))
            
        itens = ItemQuestionario.objects.filter(questionario=questionario, ativo=True)

        for item in itens:
            match item.tipo:
                case 0:
                    novaResposta = Respostas()
                    novaResposta.questionario = questionario
                    novaResposta.pergunta = item
                    novaResposta.valor = data.get(f'item-{item.id}','')
                    novaResposta.quemRespondeu = quem
                    novaResposta.save()

                case 1:
                    novaResposta = Respostas()
                    novaResposta.questionario = questionario
                    novaResposta.pergunta = item
                    novaResposta.valor = str(data.getlist(f'item-{item.id}')).replace("'","").replace('[','').replace(']','')

                    novaResposta.quemRespondeu = quem
                    novaResposta.save()

                case 2:
                    novaResposta = Respostas()
                    novaResposta.questionario = questionario
                    novaResposta.pergunta = item
                    novaResposta.valor = data.get(f'item-{item.id}','')

                    novaResposta.quemRespondeu = quem
                    novaResposta.save()

                case 3:
                    associativas = item.itemassociativo_set.all()
                    opcoes = item.opcoesitemquestionario_set.all()
                    
                    novaResposta = Respostas()
                    novaResposta.questionario = questionario
                    novaResposta.pergunta = item
                    
                    novaResposta.valor = ''

                    for a in associativas:
                        if data.get(f'associativa-{item.id}-{a.id}'):
                            novaResposta.valor += f'{opcoes[int(data.get(f'associativa-{item.id}-{a.id}'))-1].id}:{a.id}'
                            # print(f'Resposta: {novaResposta.valor}')

                            if int(data.get(f'associativa-{item.id}-{a.id}')) > 1:
                                # print('Valor atual:',int(data.get(f'associativa-{item.id}-{a.id}')))
                                novaResposta.valor +=', '

                    novaResposta.quemRespondeu = quem
                    novaResposta.save()

        messages.add_message(request, messages.SUCCESS, 'A criação foi bem sucedida!')

        return redirect('questionariosDetail', slug=questionario.slug)