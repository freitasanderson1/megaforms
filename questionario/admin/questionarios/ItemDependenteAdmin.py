from django.contrib import admin

from questionario.models import ItemDependente


@admin.register(ItemDependente)
class ItemDependenteAdmin(admin.ModelAdmin):
    list_display = ('id','perguntaChave','pergunta','opcao','ativo')
    search_fields = ['id','perguntaChave','pergunta','opcao']
    autocomplete_fields = ['perguntaChave','pergunta','opcao']
    icon_name='drag_handle'