from django.views import View
from django.contrib.auth.models import User
from cadastro.models import Perfil
class BasePermissoesView(View):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            usuario =  User.objects.get(id=request.session["_auth_user_id"])
            # print(f'User Logado:{usuario.get_full_name()}')
            
        try:
            self.perfil = Perfil.objects.get(pessoa__user=usuario)
        except:
            self.perfil = None

        self.ehEstagiario = request.user.groups.filter(name="Estagiários_Cecane").exists()
        self.ehGestor = request.user.groups.filter(name="Questionário_Gestor").exists()
        self.ehSuperUser = request.user.is_superuser
        
        if self.ehEstagiario or self.ehGestor or self.ehSuperUser:
            self.temPermissaoBase = True
        else:
            self.temPermissaoBase = False

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['temPermissaoBase'] = self.temPermissaoBase
        context['ehEstagiario'] = self.ehEstagiario
        context['ehGestor'] = self.ehGestor
        context['ehSuperUser'] = self.ehSuperUser
        context['perfil'] = self.perfil

        return context
