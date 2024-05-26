##### Questionários
from siteCecane.admin.questionarios.ItemQuestionarioAdmin import ItemQuestionarioAdmin
from siteCecane.admin.questionarios.QuemRespondeuAdmin import QuemRespondeuAdmin
from siteCecane.admin.questionarios.TipoQuestionariosAdmin import TipoQuestionarioAdmin
from siteCecane.admin.questionarios.OpcoesItemQuestionarioAdmin import OpcoesItemQuestionarioAdmin
from siteCecane.admin.questionarios.RespostaAdmin import RespostasAdmin
from siteCecane.admin.questionarios.RespostaQuestionarioAdmin import RespostasQuestionarioAdmin
# from siteCecane.admin.questionarios.RespostaAlternativaAdmin import RespostasAlternativoAdmin
########

###### Noticias
from siteCecane.admin.noticias.NoticiaAdmin import NoticiaAdmin
from siteCecane.admin.noticias.SlideshowAdmin import SlideshowAdmin
#######

####### Repositorio
from siteCecane.admin.repositorio.TipoDocumentoAdmin import TipoDocumentoAdmin
from siteCecane.admin.repositorio.DocumentoAdmin import DocumentoAdmin

from django.contrib import admin
from django_summernote.utils import get_attachment_model 
admin.site.unregister(get_attachment_model())