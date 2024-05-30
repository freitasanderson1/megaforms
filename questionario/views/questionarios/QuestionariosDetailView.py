from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.db.models import Q

from questionario.forms import QuestionarioForm
from questionario.models import TipoQuestionario, ItemQuestionario, RespostasQuestionario, QuemRespondeu
from AGF.models.Escola import Escola
from questionario.models.gestao.questionarios.RespostasAlternativoQuestionario import RespostasAlternativoQuestionario

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
        camposIgnorar = ['csrfmiddlewaretoken','escola','search_terms','nome','sobrenome','telefone','email','cidade','cargo','dataAniversario']

        if request.method == 'POST':

            tipoQuestionario = TipoQuestionario.objects.get(slug=kwargs["slug"])
            #### Escolar ###
            if tipoQuestionario.tipoDoQuestionario == 0:

                tamQuestionario = len(ItemQuestionario.objects.filter(questionario=tipoQuestionario))
                tamRequest = len(request.POST) - 3

                escola = Escola.objects.get(id=request.POST.get('escola'))
                # print(f'Questionario: {tamQuestionario}')
                # print(f'Request:{tamRequest}')

                if tamRequest < tamQuestionario:
                    messages.add_message(request, messages.ERROR, 'A criação foi mal-sucedida, responda todas as questões!')

                    return redirect('questionario:questionariosDetail', slug=kwargs["slug"])

                try:
                    questionarioRespondido = RespostasQuestionario.objects.filter(escola=escola, questionario=tipoQuestionario)
                    # print(f'Respostas: {questionarioRespondido}')
                except:
                    questionarioRespondido = None

                if questionarioRespondido:
                    messages.add_message(request, messages.ERROR, 'A criação foi mal-sucedida, já existe um questionário deste tipo respondido!')

                    return redirect('questionario:questionariosDetail', slug=kwargs["slug"])

                listaRespostas = list()
                for campo, valor in request.POST.items():
                    respostas = RespostasQuestionario()
                    # print(f'Valor de Kwargs: {kwargs["slug"]}')
                    # print(campo, valor)
                    if campo != 'csrfmiddlewaretoken' and campo != 'escola' and campo != 'search_terms':
                        respostas.escola = escola
                        respostas.questionario = tipoQuestionario
                        respostas.pergunta = ItemQuestionario.objects.get(id=campo)
                        respostas.valor = int(valor)
                        respostas.quemRespondeu = request.user
                        # print(respostas)
                        listaRespostas.append(respostas)

                bulk_msj = RespostasQuestionario.objects.bulk_create(listaRespostas)
            ###### CAE #######
            elif tipoQuestionario.tipoDoQuestionario == 1:
                print(f'Vamo brincar: {len(request.POST)-1} - {request.POST}')

                chaves = request.POST

                chaves._mutable = True

                perguntas = ItemQuestionario.objects.filter(questionario=tipoQuestionario)

                tamQuestionario = len(perguntas)-9
                tamRequest = len(request.POST)-7

                print(tamRequest,tamQuestionario)
                

                if tamRequest < tamQuestionario:
                    messages.add_message(request, messages.ERROR, f'A criação foi mal-sucedida, responda todas as questões!')

                    return redirect('questionario:questionariosDetail', slug=kwargs["slug"])

                jaRespondeu = RespostasAlternativoQuestionario.objects.filter(
                    Q(quemRespondeu__email=chaves["email"])&
                    Q(quemRespondeu__telefone=chaves["telefone"]),
                    questionario=tipoQuestionario)

                if jaRespondeu:
                    messages.add_message(request, messages.ERROR, f'A criação foi mal-sucedida, já existe respostas vindo deste email ({chaves["email"]}) e telefone ({chaves["telefone"]}) para este questionário!')

                    return redirect('questionario:questionariosDetail', slug=kwargs["slug"])
                nomeCompleto = chaves["nome"].split(' ')
                nome, sobrenome = np.array_split(nomeCompleto, 2)

                quemRespondeu = QuemRespondeu()
                quemRespondeu.nome = str(nome).replace("'","").replace('[','').replace(']','')
                quemRespondeu.sobrenome = str(sobrenome).replace("'","").replace('[','').replace(']','')
                quemRespondeu.telefone = chaves["telefone"]
                quemRespondeu.email = chaves["email"]
                quemRespondeu.cidade = chaves["cidade"]
                quemRespondeu.cargo = chaves["cargo"]
                quemRespondeu.dataAniversario = chaves['dataAniversario']
                quemRespondeu.save()

                # print(quemRespondeu)
                if str(request.POST.getlist('2')).replace("'","").replace('[','').replace(']','') == 'Não':
                    chaves['2.1'] = ''

                if str(request.POST.getlist('8')).replace("'","").replace('[','').replace(']','') == 'Não faço parte de outro conselho':
                    chaves['8.1'] = ''

                if str(request.POST.getlist('17')).replace("'","").replace('[','').replace(']','') in ['Não' , 'Não sei informar']:
                    chaves['17.1'] = ''

                if str(request.POST.getlist('19')).replace("'","").replace('[','').replace(']','') in  ['Não','Não sei informar']:
                    chaves['19.1'] = ''
                
                if str(request.POST.getlist('22')).replace("'","").replace('[','').replace(']','') == 'Não':
                    chaves['22.1'] = ''

                if str(request.POST.getlist('23')).replace("'","").replace('[','').replace(']','') == 'Não':
                    chaves['23.1'] = ''

                if str(request.POST.getlist('30')).replace("'","").replace('[','').replace(']','') == 'Não':
                    chaves['30.1'] = ''
                
                if str(request.POST.getlist('31')).replace("'","").replace('[','').replace(']','') == 'Não':
                    chaves['31.1'] = ''
                
                if str(request.POST.getlist('40')).replace("'","").replace('[','').replace(']','') == 'Não':
                    chaves['40.1'] = ''
                 
                listaChaves = ['1', '2', '2.1', '3', '4','5', '6', '7', '8', '8.1', '9','10', '11', '12', '13', '14', '15', '16', '17', '17.1', '18', '19', '19.1', '20', '21', 
                               '22', '22.1', '23', '23.1', '24', '25', '26', '27', '28', '29',  '30', '30.1', '31', '31.1', '32', '33', '34', '35', '36', '37', 
                               '38', '39',  '40', '40.1', '41', '42']
                
                chavesQuestionario = dict()

                for chave in listaChaves:
                    chavesQuestionario[chave] = str(request.POST.getlist(chave)).replace("'","").replace('[','').replace(']','')
                    if '.' not in str(chave):
                        if not chavesQuestionario[chave]:
                            messages.add_message(request, messages.ERROR, f'Você esqueceu de responder a questão {chave}, por favor responda todas as questões!')
                            quemRespondeu.delete()
                            return redirect('questionario:questionariosDetail', slug=kwargs["slug"])
                        
                    if '.' in str(chave):
                        if not chavesQuestionario[chave]:
                            chaveSuperior = chave.split('.')[0]
                            if chavesQuestionario[chaveSuperior] not in ['Não' , 'Não sei informar','Não faço parte de outro conselho']:
                                messages.add_message(request, messages.ERROR, f'Você esqueceu de responder a questão {chave}, por favor responda todas as questões!')
                                quemRespondeu.delete()
                                return redirect('questionario:questionariosDetail', slug=kwargs["slug"])
                        
                        
                    print(f'Chave: {chave} Valor: {chavesQuestionario[chave]}')

                # print(f'Novas Chaves {chavesQuestionario}')

                listaRespostas = list()

                for index, chave in enumerate(chavesQuestionario):

                    valor = chavesQuestionario[chave]
                    respostas = RespostasAlternativoQuestionario()



                    if chave not in camposIgnorar:
                        # print(f'Index:{index}- Pergunta:{perguntas[index].descricao}')
                        # print(f'Campo:{chave} - Valor:{str(chavesQuestionario[chave])}')
                        respostas.questionario = tipoQuestionario
                        respostas.pergunta = perguntas[index]
                        respostas.valor = chavesQuestionario[chave]


                        respostas.quemRespondeu = quemRespondeu
                        listaRespostas.append(respostas)

                bulk_msj = RespostasAlternativoQuestionario.objects.bulk_create(listaRespostas)
                if not bulk_msj:
                    messages.add_message(request, messages.ERROR, 'A criação foi mal-sucedida, houve um erro ao tentar salvar suas respostas. Por favor, tente novamente!')
                    quemRespondeu.delete()
                    return redirect('questionario:questionariosDetail', slug=kwargs["slug"])
                
                print(f'Respostas: {bulk_msj}')
            ####### Agricultores #########
            elif tipoQuestionario.tipoDoQuestionario == 2:
                print(f'Vamo brincar: {len(request.POST)-1} - {request.POST}')

                chaves = request.POST

                chaves._mutable = True

                perguntas = ItemQuestionario.objects.filter(questionario=tipoQuestionario)

                tamQuestionario = len(perguntas)-4
                tamRequest = len(request.POST)-7

                # print(tamRequest,tamQuestionario)
                

                if tamRequest < tamQuestionario:
                    messages.add_message(request, messages.ERROR, f'A criação foi mal-sucedida, responda todas as questões!')

                    return redirect('questionario:questionariosDetail', slug=kwargs["slug"])

                jaRespondeu = RespostasAlternativoQuestionario.objects.filter(
                    Q(quemRespondeu__email=chaves["email"])&
                    Q(quemRespondeu__telefone=chaves["telefone"]),
                    questionario=tipoQuestionario)

                if jaRespondeu:
                    messages.add_message(request, messages.ERROR, f'A criação foi mal-sucedida, já existe respostas vindo deste email ({chaves["email"]}) e telefone ({chaves["telefone"]}) para este questionário!')

                    return redirect('questionario:questionariosDetail', slug=kwargs["slug"])

                nomeCompleto = chaves["nome"].split(' ')
                nome, sobrenome = np.array_split(nomeCompleto, 2)

                quemRespondeu = QuemRespondeu()
                quemRespondeu.nome = str(nome).replace("'","").replace('[','').replace(']','')
                quemRespondeu.sobrenome = str(sobrenome).replace("'","").replace('[','').replace(']','')
                quemRespondeu.telefone = chaves.get("telefone")
                quemRespondeu.email = chaves.get("email")
                quemRespondeu.cidade = chaves.get("cidade")
                quemRespondeu.cargo = ' '
                quemRespondeu.dataAniversario = chaves.get('dataAniversario')
                quemRespondeu.save()

                # print(quemRespondeu)
                if str(request.POST.getlist('6')).replace("'","").replace('[','').replace(']','') == 'Não':
                    chaves['6.1'] = ''

                if str(request.POST.getlist('7')).replace("'","").replace('[','').replace(']','') == 'Não':
                    chaves['7.1'] = ''

                if str(request.POST.getlist('11')).replace("'","").replace('[','').replace(']','') == 'Não':
                    chaves['11.1'] = ''

                if str(request.POST.getlist('12')).replace("'","").replace('[','').replace(']','') == 'Não':
                    chaves['12.1'] = ''
                 
                listaChaves = ['1', '2', '3', '4','5', '6', '6.1', '7', '7.1','8', '9','10', '11', '11.1','12', '12.1', '13', '14', '15', '16', '17', '18', '19', '20']
                
                chavesQuestionario = dict()

                for chave in listaChaves:
                    chavesQuestionario[chave] = str(request.POST.getlist(chave)).replace("'","").replace('[','').replace(']','')
                    print(f'Chave: {chave} Valor: {chavesQuestionario[chave]}')

                print(f'Novas Chaves {chavesQuestionario}')

                listaRespostas = list()

                for index, chave in enumerate(chavesQuestionario):

                    valor = chavesQuestionario[chave]
                    respostas = RespostasAlternativoQuestionario()



                    if chave not in camposIgnorar:
                        # print(f'Index:{index}- Pergunta:{perguntas[index].descricao}')
                        # print(f'Campo:{chave} - Valor:{str(chavesQuestionario[chave])}')
                        respostas.questionario = tipoQuestionario
                        respostas.pergunta = perguntas[index]
                        respostas.valor = chavesQuestionario[chave]


                        respostas.quemRespondeu = quemRespondeu
                        listaRespostas.append(respostas)

                bulk_msj = RespostasAlternativoQuestionario.objects.bulk_create(listaRespostas)
                # print(f'Respostas: {listaRespostas}')

            ####### Gestão AF ######
            elif tipoQuestionario.tipoDoQuestionario == 3:
                print(f'Vamo brincar: {len(request.POST)-1} - {request.POST}')

                chaves = request.POST

                perguntas = ItemQuestionario.objects.filter(questionario=tipoQuestionario)

                tamQuestionario = len(perguntas)
                tamRequest = len(request.POST)-7

                print(tamRequest,tamQuestionario)
                

                # if tamRequest != tamQuestionario:
                #     messages.add_message(request, messages.ERROR, f'A criação foi mal-sucedida, responda todas as questões!')

                #     return redirect('questionario:questionariosDetail', slug=kwargs["slug"])

                jaRespondeu = RespostasAlternativoQuestionario.objects.filter(
                    Q(quemRespondeu__email=chaves["email"])&
                    Q(quemRespondeu__telefone=chaves["telefone"]),
                    questionario=tipoQuestionario)

                if jaRespondeu:
                    messages.add_message(request, messages.ERROR, f'A criação foi mal-sucedida, já existe respostas vindo deste email ({chaves["email"]}) e telefone ({chaves["telefone"]}) para este questionário!')

                    return redirect('questionario:questionariosDetail', slug=kwargs["slug"])

                quemRespondeu = QuemRespondeu()
                quemRespondeu.nome = chaves["nome"]
                quemRespondeu.sobrenome = chaves["sobrenome"]
                quemRespondeu.telefone = chaves["telefone"]
                quemRespondeu.email = chaves["email"]
                quemRespondeu.cidade = chaves["cidade"]
                quemRespondeu.cargo = chaves["cargo"]
                quemRespondeu.save()

                # print(quemRespondeu)

                listaRespostas = list()

                for index, chave in enumerate(chaves, start=-7):

                    valor = request.POST.getlist(chave)
                    respostas = RespostasAlternativoQuestionario()



                    if chave not in camposIgnorar:
                        # print(f'Index:{index}- Pergunta:{perguntas[index].descricao}')
                        # print(f'Campo:{chave} - Valor:{str(request.POST.getlist(chave))}')
                        respostas.questionario = tipoQuestionario
                        respostas.pergunta = perguntas[index]
                        respostas.valor = str(request.POST.getlist(chave)).replace("'","").replace('[','').replace(']','')
                        if chaves["4"] == 'Não' and chave == '4.1':
                            respostas.valor = ''
                        respostas.quemRespondeu = quemRespondeu
                        listaRespostas.append(respostas)

                bulk_msj = RespostasAlternativoQuestionario.objects.bulk_create(listaRespostas)

            messages.add_message(request, messages.SUCCESS, 'A criação foi bem-sucedida!')

            return redirect('questionario:questionariosDetail', slug=kwargs["slug"])
        else:
            form = QuestionarioForm()

        return super().dispatch(request, *args, **kwargs)