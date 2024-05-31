from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework.routers import DefaultRouter

from cadastro.views import LoginView, SairView, CadastroView

from questionario.views import MegaFormsIndexView, NoticiasView, SobreView, RepositorioView, PoliticaPrivacidadeView
from questionario.views import QuestionariosIndexView, QuestionariosDetailView, ExportRespostasView

from questionario.views import RelatoriosQuestionariosIndexView, RelatoriosDetailView, RelatoriosComplexosDetailView

app_name = 'questionario'

urlpatterns = [

    #### SITE
    path('', MegaFormsIndexView.as_view(), name='indexSite'),
    path('noticias/', NoticiasView.as_view(), name='noticias' ),
    path('documentos/', RepositorioView.as_view(), name='repositorio'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('privacidade/', PoliticaPrivacidadeView.as_view(), name='politicaPrivacidade'),
    path('admin/', admin.site.urls),

    #Questionários
    path('questionarios/', QuestionariosIndexView.as_view(), name='questionariosIndex'),
    path('questionarios/<slug:slug>/', QuestionariosDetailView.as_view(), name='questionariosDetail'),


    #Relatórios
    path('relatorios/', RelatoriosQuestionariosIndexView.as_view(), name='relatoriosQuestionariosIndex' ),
    path('relatorios/<slug:slug>/', RelatoriosDetailView.as_view(), name='relatoriosDetail' ),
    path('relatorios/complexos/<slug:slug>/', RelatoriosComplexosDetailView.as_view(), name='relatoriosComplexosDetail' ),
    path('relatorios/export/<slug:slug>/', ExportRespostasView.as_view(), name='exportQuestionario' ),

    #Logins views
    path('login/', LoginView.as_view(), name='login'),
    path('sair/', SairView.as_view(), name='sair'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),

]

router = DefaultRouter(trailing_slash=False)
# router.register(r'api/dados_vendas',VendasApiView, basename='VendasApi')


urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)