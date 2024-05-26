from django.http import HttpResponse
from siteCecane.models import Noticia
from django.views.generic import ListView

from siteCecane.views import BasePermissoesView

class NoticiasView(BasePermissoesView,ListView):
    template_name = "siteCecane/noticias.html"
    queryset = []
    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        noticias = Noticia.objects.all().order_by('-id')

        context['noticias'] = noticias

        return context
