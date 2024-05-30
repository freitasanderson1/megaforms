from django.contrib import admin
from questionario.models import Noticia
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Noticia)

class NoticiaAdmin(SummernoteModelAdmin):
    list_display = ('titulo','subtitulo',)
    summernote_fields = ('noticia')
    icon_name='whatshot'