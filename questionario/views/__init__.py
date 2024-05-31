##BaseViews
from questionario.views.baseViews.BasePermissoesView import BasePermissoesView

#Páginas
from questionario.views.site.MegaFormsIndexView import MegaFormsIndexView
from questionario.views.site.EquipeView import EquipeView
from questionario.views.site.NoticiasView import NoticiasView
from questionario.views.site.SobreView import SobreView
from questionario.views.site.RepositorioView import RepositorioView
from questionario.views.site.PoliticaPrivacidadeView import PoliticaPrivacidadeView

##Questionários
from questionario.views.questionarios.QuestionariosIndexView import QuestionariosIndexView
from questionario.views.questionarios.QuestionariosDetailView import QuestionariosDetailView

##Relatórios
### Relatórios de Questionários
from questionario.views.relatorios.questionarios.RelatoriosQuestionariosIndexView import RelatoriosQuestionariosIndexView
from questionario.views.relatorios.questionarios.RelatoriosDetailView import RelatoriosDetailView
from questionario.views.relatorios.questionarios.RelatoriosComplexosDetailView import RelatoriosComplexosDetailView
###
from questionario.views.relatorios.questionarios.ExportRespostasView import ExportRespostasView