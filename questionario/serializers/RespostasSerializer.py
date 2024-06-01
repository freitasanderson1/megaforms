from rest_framework import serializers
from questionario.models import Respostas

from questionario.serializers import QuemRespondeuSerializer

class RespostasSerializer(serializers.ModelSerializer):
  
  quemRespondeu = QuemRespondeuSerializer()

  class Meta:

    model = Respostas
    fields = '__all__'