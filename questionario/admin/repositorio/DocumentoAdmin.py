from django.contrib import admin

from questionario.models import Documento

@admin.register(Documento)

class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('nome','tipo','arquivo','quemCadastrou','ativo')
    autocomplete_fields = ('quemCadastrou',)
    readonly_fields = ['dataCadastro', 'dataAlteracao']
    icon_name = 'description'