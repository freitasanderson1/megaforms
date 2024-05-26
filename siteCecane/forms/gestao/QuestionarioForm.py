from django import forms
from django.forms import modelformset_factory
from django.forms import formset_factory
from siteCecane.models import RespostasQuestionario,ItemQuestionario,TipoQuestionario

class QuestionarioForm(forms.ModelForm):
    class Meta:
        model = RespostasQuestionario
        fields = ['escola', 'questionario', 'pergunta', 'valor']

