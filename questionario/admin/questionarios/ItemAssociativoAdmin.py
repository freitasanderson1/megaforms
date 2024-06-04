from django.contrib import admin

from questionario.models import ItemAssociativo


@admin.register(ItemAssociativo)
class ItemAssociativoAdmin(admin.ModelAdmin):
    list_display = ('id','opcao','valor')
    search_fields = ['id','opcao','valor']
    autocomplete_fields = ['opcao']
    icon_name='drag_handle'