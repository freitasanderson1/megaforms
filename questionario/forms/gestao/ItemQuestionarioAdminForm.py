from django import forms

from questionario.models import ItemQuestionario

class ItemQuestionarioAdminForm(forms.ModelForm):

    class Meta:
        model = ItemQuestionario
        fields = ['questionario','descricao','tipo']
