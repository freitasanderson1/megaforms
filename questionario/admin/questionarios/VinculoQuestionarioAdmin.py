from django.contrib import admin
from questionario.models import VinculoQuestionario

@admin.register(VinculoQuestionario)
class VinculoQuestionarioAdmin(admin.ModelAdmin):
    list_display = ('id','questionarioPre','questionarioPos','ativo')
    search_fields = ['id','questionarioPre','questionarioPos']

    autocomplete_fields = ['questionarioPre','questionarioPos']

    icon_name = 'dehaze'