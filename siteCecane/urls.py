from django.urls import path
from siteCecane.views import CecaneIndexView, EquipeView, NoticiasView, SobreView, RepositorioView, PoliticaPrivacidadeView
from siteCecane.views import QuestionariosIndexView, QuestionariosDetailView, RespostasEscolasIndexView, RespostasEscolasDetailView, RespostasComplexView, ExportRespostasView

from siteCecane.views import RelatoriosQuestionariosIndexView, RelatoriosDetailView, RelatoriosComplexosDetailView
from cadastro.views import LoginView, SairView, CadastroView

app_name = 'siteCecane'

urlpatterns = [

    #### SITE
    path('', CecaneIndexView.as_view(), name='indexSite'),
    path('noticias/', NoticiasView.as_view(), name='noticias' ),
    path('documentos/', RepositorioView.as_view(), name='repositorio'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('privacidade/', PoliticaPrivacidadeView.as_view(), name='politicaPrivacidade'),

    # path('eventos/', EventosView.as_view(), name='eventos'),
    path('equipe/',EquipeView.as_view(), name='equipe'),


    #Questionários
    path('questionarios/', QuestionariosIndexView.as_view(), name='questionariosIndex'),
    path('questionarios/<slug:slug>/', QuestionariosDetailView.as_view(), name='questionariosDetail'),
    path('questionarios/respostas/<slug:slug>/', RespostasEscolasIndexView.as_view(), name='respostasIndex'),
    path('questionarios/respostas/<slug:slug>/<int:pk>/', RespostasEscolasDetailView.as_view(), name='respostasDetail'),
    path('questionarios/respostas/complex/<slug:slug>/', RespostasComplexView.as_view(), name='respostasComplexasDetail'),


    #Relatórios
    path('relatorios/', RelatoriosQuestionariosIndexView.as_view(), name='relatoriosQuestionariosIndex' ),
    path('relatorios/<slug:slug>/', RelatoriosDetailView.as_view(), name='relatoriosDetail' ),
    path('relatorios/complexos/<slug:slug>/', RelatoriosComplexosDetailView.as_view(), name='relatoriosComplexosDetail' ),
    path('relatorios/export/<slug:slug>/', ExportRespostasView.as_view(), name='exportQuestionario' ),





    #Logins views
    path('login/', LoginView.as_view(), name='login'),
    path('sair/', SairView.as_view(), name='sair'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),



    # path('equipe/', equipe), #Equipe
    # path('sobre/', sobre), #Sobre
    # path('eventos/', eventos), #Eventos
    # path('noticias/', noticias), #Notícias

]