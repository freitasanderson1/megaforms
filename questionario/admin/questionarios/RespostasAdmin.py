from django.contrib import admin
from django import forms

from questionario.models import Respostas


@admin.register(Respostas)
class RespostasAdmin(admin.ModelAdmin):
    autocomplete_fields = ['quemRespondeu', 'questionario','pergunta']
    list_display = ('id','questionario','pergunta','valor','quemRespondeu','dataCadastro','dataAlteracao')
    list_filter = ('questionario','pergunta__tipo')
    icon_name='drag_handle'
    actions = ['criarRespostasQuestionarioEscolar']
    list_per_page = 10000