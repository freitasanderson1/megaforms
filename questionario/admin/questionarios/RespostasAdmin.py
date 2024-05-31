from django.contrib import admin
from django import forms

from questionario.models import Respostas


@admin.register(Respostas)
class RespostasAdmin(admin.ModelAdmin):
    list_display = ('id','questionario','pergunta','valor','quemRespondeu','dataCadastro','dataAlteracao')
    readonly_fields = ['quemRespondeu',]
    icon_name='drag_handle'
    actions = ['criarRespostasQuestionarioEscolar']
    list_per_page = 10000