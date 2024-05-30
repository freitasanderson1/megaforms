from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from cadastro.forms.cadastroForm import CadastroForm
from cadastro.models.Pessoa import Pessoa

class CadastroView(CreateView):
    template_name = 'cadastro/cadastro.html'
    form_class = CadastroForm
    model = User
    textSucess = ''
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context['form'] = self.form_class
        context['textSucess'] = self.textSucess

        return context

    def dispatch(self, request, *args, **kwargs):
        usuario = request.user

        if request.POST:
            try:
                check_existe_usuario = User.objects.get(username=request.POST['cpf'])
            except:
                check_existe_usuario = None

            if check_existe_usuario:
                messages.add_message(request, messages.ERROR, 'Ocorreu um erro ao realizar seu cadastro, um usuário com este CPF já existe!')
                return redirect('questionario:cadastro')

            print(request.POST)

            novo_usuario = User()

            novo_usuario.first_name = request.POST.get('nome')
            novo_usuario.last_name = request.POST.get('sobrenome')
            novo_usuario.username = request.POST.get('cpf')
            novo_usuario.email = request.POST.get('email')
            senha = request.POST.get('senha')
            senhaConfirma = request.POST.get('senhaConfirma')

            print(novo_usuario)
            
            if senha != senhaConfirma:
                print('Senha não é igual')
                messages.add_message(request, messages.ERROR, 'Ocorreu um erro ao realizar seu cadastro, as senhas não são iguais!')
                return redirect('questionario:cadastro')

            else:
                senha_criptografada = make_password(password=request.POST['senha'], salt=None, hasher='pbkdf2_sha256')
                corresponde = check_password(password=senha, encoded=senha_criptografada)

                if corresponde:
                    novo_usuario.password = senha_criptografada
                    print('Passou!')
                    
                    novo_usuario.save()

                    nova_pessoa = Pessoa()
                    nova_pessoa.user = novo_usuario
                    nova_pessoa.nomeCompleto = f'{novo_usuario.get_full_name()}'
                    nova_pessoa.cpf = novo_usuario.username
                    nova_pessoa.email = novo_usuario.email
                    nova_pessoa.contato = f'({request.POST["ddd"]}){request.POST["telefone"]}'
                    nova_pessoa.sexo = request.POST['sexo']
                    nova_pessoa.dataNascimento = request.POST['dataNascimento']
                    nova_pessoa.save()

                    print(nova_pessoa)

                    self.textSucess = 'Sucesso'

                    messages.add_message(request, messages.SUCCESS, self.textSucess)
                else:
                    messages.add_message(request, messages.ERROR, 'Ocorreu um erro ao realizar seu cadastro, tente novamente!')


                    

        if usuario.is_authenticated:

            print(f'Usuario: {usuario.id}')
            return redirect('questionario:indexSite')



        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):


        return redirect('questionario:login')