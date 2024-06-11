##### Questionários
from questionario.admin.questionarios.ItemQuestionarioAdmin import ItemQuestionarioAdmin
from questionario.admin.questionarios.QuemRespondeuAdmin import QuemRespondeuAdmin
from questionario.admin.questionarios.TipoQuestionariosAdmin import TipoQuestionarioAdmin
from questionario.admin.questionarios.OpcoesItemQuestionarioAdmin import OpcoesItemQuestionarioAdmin
from questionario.admin.questionarios.RespostasAdmin import RespostasAdmin
from questionario.admin.questionarios.ItemAssociativoAdmin import ItemAssociativoAdmin
from questionario.admin.questionarios.ItemCorretoAdmin import ItemCorretoAdmin
from questionario.admin.questionarios.VinculoQuestionarioAdmin import VinculoQuestionarioAdmin
########

###### Noticias
from questionario.admin.noticias.NoticiaAdmin import NoticiaAdmin
from questionario.admin.noticias.SlideshowAdmin import SlideshowAdmin
#######

####### Repositorio
from questionario.admin.repositorio.TipoDocumentoAdmin import TipoDocumentoAdmin
from questionario.admin.repositorio.DocumentoAdmin import DocumentoAdmin

from django.contrib import admin
from django_summernote.utils import get_attachment_model 
admin.site.unregister(get_attachment_model())