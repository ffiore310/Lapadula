# BANCO DE DADOS
from funcaocolorida import tabela_distancia_colorida
from funcoes import adiciona_em_ordem, normaliza, sorteia_pais, haversine, tabela_distancias
from dados import DADOS

raio_Terra = 6371

# ABERTURA JOGO
print('  =============================  \n|                               |\n|  Bem-vindo ao Insper Paises!  |\n|                               |\n  ==== Design de Software =====\n \n Comandos:\n     dica       - entra no mercado de dicas\n     desisto    - desiste da rodada\n     inventario - exibe sua posicao\n')
inicializa = True

while inicializa:
  
  dicionario_paises = normaliza(DADOS)

  cont_sorteado = sorteia_pais(DADOS)
  pais_sorteado = sorteia_pais(DADOS[cont_sorteado])
  lista_inventario = []
  lista_paises = []
  tentativas = 20

  roda_while = True
  print(pais_sorteado)
  print('Um pais foi escolido! \nTente adivinhar! \nVoce tem {0} tentativa(s)\n'.format(tentativas))

  while roda_while:
      
      resposta = input('Qual o seu palpite?: ')

    # ACERTOU O JOGO
      if resposta.lower() == pais_sorteado:
          print('Parabens! Voce acertou em {} tentativa(s)'.format(20-tentativas+1))
          roda_while = False
          a = True
          while a:
            novamente = input('\nDeseja jogar novamente? [s|n]')
            if novamente == 'n':
                roda_while = False
                inicializa = False
                a = False
            elif novamente != 's':
                print('Insira apenas [s|n]')
            else:
              a= False

    # DESISTIU DO JOGO

      elif resposta == 'desisto':
              certeza = input('Tem certeza que deseja desistir da rodada? [s|n]')
              if certeza == 's':
                  roda_while = False
                  print('Que deselegante desistir, o pais era: {}'.format(pais_sorteado))

                  a = True
                  while a:
                    novamente = input('\nDeseja jogar novamente? [s|n]')
                    if novamente == 'n':
                      roda_while = False
                      inicializa = False
                      a = False
                    elif novamente != 's':
                      print('Insira apenas [s|n]')
                    else:
                      a= False

              
      # ACABAR AS TENTATIVAS

      elif tentativas == 1:
          print('Vixe! Parece que acabaram as tentativas :\ \n Voce perdeu, o pais era: {}'.format(pais_sorteado))
          roda_while = False
          a = True
          while a:
            novamente = input('\nDeseja jogar novamente? [s|n]')
            if novamente == 'n':
              roda_while = False
              inicializa = False
              a = False
            elif novamente != 's':
               print('Insira apenas [s|n]')
            else:
              a= False

    # MERCADO DE DICAS

      elif resposta == 'dica':
          print('dica')

    # PRINT INVENTARIO

      elif resposta == 'inventario':
          inventario = tabela_distancia_colorida(lista_inventario)
          print('\nDistancias :\n {}'.format(inventario))

    # CHUTE FOR DIFERENTE DA RESPOSTA

      elif resposta.lower() in dicionario_paises:

        #CALCULAR AS DISTANCIAS

          lat1 = dicionario_paises[resposta.lower()]['geo']['latitude']
          long1 = dicionario_paises[resposta.lower()]['geo']['longitude'] 
          lat2 = dicionario_paises[pais_sorteado]['geo']['latitude']
          long2 = dicionario_paises[pais_sorteado]['geo']['longitude']
          distancia = haversine(raio_Terra, lat1, long1, lat2, long2)
          distancia = int(distancia)
        
        # PAIS JA FOI CHUTADO

          if resposta.lower() in lista_paises:
              inventario = tabela_distancia_colorida(lista_inventario)
              print('\nInventario :\n {}'.format(inventario))
              print('Este pais ja foi inserido! Insira um novo')
              print('Você tem {} tentativa(s)'.format(tentativas))

        # PAIS NAO FOI CHUTADO
              
          else:
              lista_paises.append(resposta.lower())
              tentativas -= 1
              lista_inventario = adiciona_em_ordem(resposta.lower(), distancia, lista_inventario)
              inventario = tabela_distancia_colorida(lista_inventario)
              print('\nInventario :\n {}'.format(inventario))
              print('Você tem {} tentativa(s)'.format(tentativas))

  # SE O PAIS FOR DESCONHECIDO

      else:
          print('País desconhecido')


print('Que pena! Espero que tenha se divertido!\n Ate a proxima ;)')