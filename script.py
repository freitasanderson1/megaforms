from questionario.models import Respostas, OpcoesItemQuestionario, ItemAssociativo
import numpy as np


# countResp = 0
# for resposta in Respostas.objects.filter(pergunta__id=7):
#   if len(resposta.valor.split(',')) > 1:
#     countResp +=1
#     print(f'Quem: {resposta.quemRespondeu}')

# print(f'Total: {countResp}')

# for resposta in Respostas.objects.filter(pergunta__id=7,pergunta__tipo=3):

#   if resposta.valor:
#       for index,ids in enumerate(resposta.valor.split(',')):
#         antes = 2 if index == 0 else index-1
#         depois = 0 if index == 2 else index+1
#         print(f'Procurando...')
#         if resposta.valor.split(',')[index] == resposta.valor.split(',')[antes] or resposta.valor.split(',')[index] == resposta.valor.split(',')[depois]:
#           print(f'ACHEI!!!!')


  # print(f'Valor:{resposta.id} - {len(resposta.valor)}')

    # for i in resposta.valor.split(','):
    #   for a in i.split(':'):
    #     print(a)
        # if len(a) > 2:
          # a = a.replace(f'{a[:-2]}{a[-2:]}',f'{a[:-2]},{a[-2:]}')
          # print(f'Erro: {a[-2:]} -Correto: {a[:-2]} I: {i}- Resposta: {resposta.valor}')
          # resposta.valor = resposta.valor.replace(f'{a[:-2]}{a[-2:]}',f'{a[:-2]},{a[-2:]}')
          # print(f"A:{a} Acorreto: {a.replace(f'{a[:-2]}{a[-2:]}',f'{a[:-2]},{a[-2:]}')} Resposta: {resposta.valor}")
          # resposta.save()

  # resposta.valor = resposta.valor.replace(', ',',')

  # for ids in resposta.valor.split(','):
    
  #   listpk = np.array_split(ids.split(':'), 2)

  #   # print(f'Lista: {len(listpk[0])}-{listpk[0]}')

  #   if len(listpk[0]) == 2:
  #     # print(f'Lista: {listpk[0]}')
  #     pk, pk2 = np.split(listpk[0],2)

  #   # pk, pk2 = np.array_split(ids.split(':'), 2)
  #     # print(f'PK: {int(pk[0])} e PK2: {int(pk2[0])}')

  #     if str(int(pk[0])-1) in pk2[0]:
  #       pk3 = int(pk[0])-1
  #       pk2 = str(pk2).replace(str(pk3),'') 
  #       # print(f'Pode ta aqui ein: {int(pk[0])-1}')

      
  #     if str(int(pk[0])+1) in pk2[0]:
  #       pk3 = int(pk[0])+1
  #       pk2 = str(pk2).replace(str(pk3),'').replace("['","").replace("']","") 

  #       # print(f'Pode ta aqui 2: {int(pk[0])+1}')

  #     resposta.valor = resposta.valor.replace(f"{pk2}{pk3}",f"{pk2},{pk3}")

  #     print(f'PK:{pk[0]} PK2:{pk2} PK3:{pk3} Valor:{resposta.valor}')

  #     # resposta.save()

  # # if len(resposta.valor) > 0 and resposta.valor[-1] == ',':
  # #   resposta.valor = resposta.valor[0:len(resposta.valor)-1]
  # #   print(f'Resposta: {resposta.valor}')

  #   # resposta.save()