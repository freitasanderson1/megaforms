from django.contrib import admin
from django import forms
from django.contrib.admin.options import StackedInline
from siteCecane.models import ItemQuestionario, OpcoesItemQuestionario

class OpcoesItemQuestionarioInline(StackedInline):
    extra = 1
    model = OpcoesItemQuestionario

@admin.register(ItemQuestionario)
class ItemQuestionarioAdmin(admin.ModelAdmin):
    list_display = ('id','questionario','descricao','ativo')
    icon_name = 'dehaze'
    inlines = [
        OpcoesItemQuestionarioInline
    ]
    actions = ['criarOpcoesQuestionarioEscolar']
    class Media:
        js = ('assets/JS/admin/ScriptQuestionarioAdmin.js',)    
        css = {
             'all': ('assets/CSS/admin/QuestionarioAdmin.css',)
        }

    
    def criarOpcoesQuestionarioEscolar(modeladmin, request, queryset):
        for pergunta in queryset.filter(questionario__tipoDoQuestionario=0):
            opcoes = OpcoesItemQuestionario.objects.filter(pergunta=pergunta)

            if opcoes.exists():
                jaTemAlguma = True
            else:
                jaTemAlguma = False
            
            if not jaTemAlguma:
                opcaoSim = OpcoesItemQuestionario()
                opcaoSim.pergunta = pergunta
                opcaoSim.valor = 'Sim'
                opcaoSim.save()

                opcaoNao = OpcoesItemQuestionario()
                opcaoNao.pergunta = pergunta
                opcaoNao.valor = 'Não'
                opcaoNao.save()

                opcaoNSA = OpcoesItemQuestionario()
                opcaoNSA.pergunta = pergunta
                opcaoNSA.valor = 'Não se aplica'
                opcaoNSA.save()
            else:

                temSim = opcoes.filter(valor='Sim').exists()
                if not temSim:
                    opcaoSim = OpcoesItemQuestionario()
                    opcaoSim.pergunta = pergunta
                    opcaoSim.valor = 'Sim'
                    opcaoSim.save()

                temNao = opcoes.filter(valor='Não').exists()
                if not temNao:
                    opcaoNao = OpcoesItemQuestionario()
                    opcaoNao.pergunta = pergunta
                    opcaoNao.valor = 'Não'
                    opcaoNao.save()

                temNSA = opcoes.filter(valor='Não se aplica').exists()
                if not temNSA:
                    opcaoNSA = OpcoesItemQuestionario()
                    opcaoNSA.pergunta = pergunta
                    opcaoNSA.valor = 'Não se aplica'
                    opcaoNSA.save()

    criarOpcoesQuestionarioEscolar.short_description = "Criar Opões de resposta para os questionários escolares"