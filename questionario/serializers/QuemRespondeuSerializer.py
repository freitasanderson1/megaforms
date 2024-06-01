from rest_framework import serializers
from questionario.models import QuemRespondeu

class QuemRespondeuSerializer(serializers.ModelSerializer):

  class Meta:

    model = QuemRespondeu
    fields = '__all__'