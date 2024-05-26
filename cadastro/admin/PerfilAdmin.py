from django.contrib import admin

from cadastro.models import Perfil

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('id','nome','cargo','imagem','ativo')
    search_fields = ('id','nome','cargo')
    autocomplete_fields = ('pessoa',)
    icon_name = 'assignment_ind'