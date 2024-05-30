from django.contrib import admin
from questionario.models import Slideshow
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Slideshow)

class SlideshowAdmin(SummernoteModelAdmin):
    list_display = ('titulo','subtitulo',)
    summernote_fields = ('imagem')
    icon_name= 'photo_library'