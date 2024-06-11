from rest_framework import serializers
from questionario.models import ItemCorreto

class ItemCorretoSerializer(serializers.ModelSerializer):
  
  class Meta:

    model = ItemCorreto
    
    fields = '__all__'