from django.contrib import admin
from django import forms

from questionario.models import Respostas


@admin.register(Respostas)
class RespostasAdmin(admin.ModelAdmin):
    list_display = ('id','questionario','escola','quemCadastrou','quemRespondeu','pergunta','valor')
    icon_name='drag_handle'
    
    def save_model(self, request, obj, form, change):

        if not obj.quemCadastrou:
            obj.quemCadastrou = request.user

        super(RespostasAdmin, self).save_model(request, obj, form, change)