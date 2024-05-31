from django import forms
from django.forms import modelformset_factory
from django.forms import formset_factory
from questionario.models import Respostas, ItemQuestionario,TipoQuestionario

class QuestionarioForm(forms.ModelForm):
    class Meta:
        model = Respostas
        fields = ['questionario', 'pergunta', 'valor']
