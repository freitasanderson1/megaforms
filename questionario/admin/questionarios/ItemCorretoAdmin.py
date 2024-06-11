from django.contrib import admin

from questionario.models import ItemCorreto


@admin.register(ItemCorreto)
class ItemCorretoAdmin(admin.ModelAdmin):
    list_display = ('id','opcao','valor')
    search_fields = ['id','opcao','valor']
    autocomplete_fields = ['opcao']
    icon_name='drag_handle'