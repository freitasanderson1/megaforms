from django.contrib import admin
from django import forms
from django_summernote.admin import SummernoteModelAdmin, SummernoteInlineModelAdmin, SummernoteWidget

from questionario.models import QuemRespondeu, Respostas

class RespostasInline(admin.TabularInline):
    model = Respostas
    extra = 0
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)
    readonly_fields = ['questionario','pergunta',]

@admin.register(QuemRespondeu)
class QuemRespondeuAdmin(admin.ModelAdmin):
    list_display = ('retornaQuem',)
    search_fields = ['nome','sobrenome','cargo']
    inlines = [
        RespostasInline
    ]
    
    icon_name = 'record_voice_over'

    @admin.display(description='Qual questionário e quem em respondeu:')
    def retornaQuem(self,obj):
        respostas = Respostas.objects.filter(quemRespondeu=obj)
        questionario = respostas.last().questionario.nome if respostas else '(Contatar este usuário, respostas não foram salvas.)'
        # print(f'Quem: {questionario}')
        quemRespondeu = f'{questionario} - {obj.nome} {obj.sobrenome}'
    
        if obj.cargo:
            quemRespondeu += f' - {obj.cargo}'

        if obj.cidade:
            quemRespondeu += f'({obj.cidade})'

        return quemRespondeu