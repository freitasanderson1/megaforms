from django.contrib import admin

from questionario.models import OpcoesItemQuestionario


@admin.register(OpcoesItemQuestionario)
class OpcoesItemQuestionarioAdmin(admin.ModelAdmin):
    list_display = ('id','pergunta','valor')
    search_fields = ['id','pergunta','valor']
    autocomplete_fields = ['pergunta']
    icon_name='drag_handle'