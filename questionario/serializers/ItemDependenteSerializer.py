from rest_framework import serializers
from questionario.models import ItemDependente

from questionario.serializers import ItemQuestionarioSerializer

class ItemDependenteSerializer(serializers.ModelSerializer):
  
  perguntaChave = ItemQuestionarioSerializer()
  pergunta = ItemQuestionarioSerializer()

  class Meta:

    model = ItemDependente
    fields = '__all__'