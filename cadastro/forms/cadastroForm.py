from django import forms
from django.contrib.auth.models import User
from cadastro.models import Pessoa


class CadastroForm(forms.ModelForm):
    
    def __init__(self,  *args, **kwargs):
        super(CadastroForm, self).__init__(*args, **kwargs)

        for visible in self.visible_fields():

            if visible.name == 'sexo':
                visible.field.widget.attrs['class'] = 'form-select'
    class Meta:
        model = Pessoa
        fields = [
            'nomeCompleto',
            'cpf',
            'email',
            'contato',
            'sexo',
            'dataNascimento',
        ]
        