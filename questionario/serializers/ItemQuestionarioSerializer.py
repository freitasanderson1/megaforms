from rest_framework import serializers
from questionario.models import ItemQuestionario, ItemDependente, Respostas, QuemRespondeu

from questionario.serializers import OpcoesItemQuestionarioSerializer, RespostasSerializer
from questionario.serializers import ItemAssociativoSerializer, ItemCorretoSerializer, ItemDependenteSerializer

class ItemQuestionarioSerializer(serializers.ModelSerializer):
  
  dependente = ItemDependenteSerializer(source='pergunta', many=True)
  alternativas = OpcoesItemQuestionarioSerializer(source='opcoesitemquestionario_set', many=True)
  respostas = RespostasSerializer(source='respostas_set', many=True)
  associacoes = ItemAssociativoSerializer(source='itemassociativo_set', many=True)
  correto = ItemCorretoSerializer(source='itemcorreto_set', many=True)

  class Meta:

    model = ItemQuestionario
    fields = ['id','tipo','descricao','ativo','alternativas','associacoes', 'respostas','correto','dependente']