from django.contrib import admin

from siteCecane.models import OpcoesItemQuestionario


@admin.register(OpcoesItemQuestionario)
class OpcoesItemQuestionarioAdmin(admin.ModelAdmin):
    list_display = ('id','pergunta','valor')
    icon_name='drag_handle'