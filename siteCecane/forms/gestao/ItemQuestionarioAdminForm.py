from django import forms

from siteCecane.models import ItemQuestionario

class ItemQuestionarioAdminForm(forms.ModelForm):

    class Meta:
        model = ItemQuestionario
        fields = ['questionario','descricao','tipo']
