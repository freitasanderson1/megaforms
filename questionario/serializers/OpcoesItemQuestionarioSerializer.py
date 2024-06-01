from rest_framework import serializers
from questionario.models import OpcoesItemQuestionario

class OpcoesItemQuestionarioSerializer(serializers.ModelSerializer):
  
  class Meta:

    model = OpcoesItemQuestionario
    fields = '__all__'