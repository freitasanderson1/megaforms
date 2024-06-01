from rest_framework import serializers
from questionario.models import TipoQuestionario, ItemDependente, OpcoesItemQuestionario, Respostas, QuemRespondeu
from questionario.serializers import ItemQuestionarioSerializer

class QuestionarioSerializer(serializers.ModelSerializer):
  
  perguntas = ItemQuestionarioSerializer(source='itemquestionario_set', many=True)

  class Meta:

    model = TipoQuestionario
    fields = '__all__'