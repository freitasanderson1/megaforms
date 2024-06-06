from rest_framework import serializers
from questionario.models import ItemAssociativo

class ItemAssociativoSerializer(serializers.ModelSerializer):
  
  class Meta:

    model = ItemAssociativo
    
    fields = '__all__'