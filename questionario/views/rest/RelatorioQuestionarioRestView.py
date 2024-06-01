from rest_framework import viewsets
from rest_framework.response import Response

from questionario.models import TipoQuestionario

from questionario.serializers import QuestionarioSerializer

class RelatorioQuestionarioRestView(viewsets.ModelViewSet):
    serializer_class = QuestionarioSerializer

    def get_queryset(self):
        responseData = {'mensagem':'Não permitido!'}
        
        return Response(responseData)

    def list(self, request):
        responseData = {'mensagem':'Não permitido!'}
        
        return Response(responseData)
    
    def retrieve(self, request, *args, **kwargs):
        
        slug = kwargs.get('pk')
        questionario = QuestionarioSerializer(TipoQuestionario.objects.filter(slug=slug), many=True).data

        # print(f'Questionario: {questionario}')
        return Response(questionario[0])