from django.contrib import admin

from cadastro.models import Pessoa

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('user','nomeCompleto','email','ativo')
    search_fields = ('cpf','nomeCompleto','email')
    autocomplete_fields = ('user',)
    exclude = ('id',)
    icon_name = 'person'
