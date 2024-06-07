from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework.routers import DefaultRouter

from cadastro.views import LoginView, SairView, CadastroView

from questionario.views import MegaFormsIndexView, NoticiasView, SobreView, RepositorioView, PoliticaPrivacidadeView
from questionario.views import QuestionariosIndexView, QuestionariosDetailView, ExportRespostasView, RespostasDetailView, RelatorioQuestionarioView
from questionario.views import RelatorioQuestionarioRestView, QuestionarioRestView

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
    path('respostas/<slug:slug>/', RespostasDetailView.as_view(), name='respostasDetail'),


    #Relatórios
    path('relatorios/<slug:slug>/', RelatorioQuestionarioView.as_view(), name='relatoriosDetail' ),
    path('relatorios/export/<slug:slug>/', ExportRespostasView.as_view(), name='exportQuestionario' ),
    
    #Logins views
    path('login/', LoginView.as_view(), name='login'),
    path('sair/', SairView.as_view(), name='sair'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),

    path('api/questionario/<int:id>/', QuestionarioRestView.as_view(), name='questionarioCreate'),

    path('.well-known/', include('letsencrypt.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('editor/', include('django_summernote.urls')),
    
]

router = DefaultRouter(trailing_slash=False)
router.register(r'api/relatorios',RelatorioQuestionarioRestView, basename='RelatorioApi')


urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)