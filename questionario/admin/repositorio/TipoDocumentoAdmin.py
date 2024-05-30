from django.contrib import admin

from questionario.models import TipoDocumento

@admin.register(TipoDocumento)

class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ('id','nome','tipo')
    icon_name= 'chrome_reader_mode'