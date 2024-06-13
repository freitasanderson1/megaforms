from rest_framework import serializers
from questionario.models import ItemDependente

class ItemDependenteSerializer(serializers.ModelSerializer):

  class Meta:

    model = ItemDependente
    fields = '__all__'