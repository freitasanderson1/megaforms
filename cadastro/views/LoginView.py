from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from cadastro.models import Pessoa
class LoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'cadastro/login.html'
    
    def form_valid(self, form):
        # print(self.request.POST)
        super().form_valid(form)
        messages.success(self.request, "Login bem-sucedido.")
        self.registraParametrosSessaoPessoa(self.request.POST.get('username'))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Credenciais inválidas. Verifique seu CPF e senha.")
        return super().form_invalid(form)
    

    def registraParametrosSessaoPessoa(self, userID):
		## CONFS DEFAULT
        self.request.session['eFake'] = False

        pessoa = Pessoa.objects.get(user__username=userID)

		## PARAMETROS
        self.request.session['idPessoa'] = pessoa.pk
        self.request.session['idUser'] = pessoa.user.pk
        self.request.session['idUserFake'] = pessoa.user.pk
        self.request.session['nomeUserFirstName'] = pessoa.user.first_name
        self.request.session['cpfPessoa'] = pessoa.cpf
        self.request.session['nomePessoa'] = pessoa.nomeCompleto
        self.request.session['emailPessoa'] = pessoa.email
