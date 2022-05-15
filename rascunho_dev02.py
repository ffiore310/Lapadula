# RASCUNHO DESENVOLVEDOR 2 - ARTHUR CALABRESI


# BANCO DE DADOS
from funcoes import adiciona_em_ordem, coloca_na_lista, normaliza, sorteia_letra, sorteia_pais, haversine, tabela_distancias, mercado_dicas

from dados import DADOS

from random import choice

raio_Terra = 6371

# ABERTURA JOGO

dicionario_paises = normaliza(DADOS)

cont_sorteado = sorteia_pais(DADOS)
pais_sorteado = sorteia_pais(DADOS[cont_sorteado])
lista_inventario = []
lista_paises = []
lista_cores = []
lista_letras = []
lista_letras_usadas = []
lista_cores_bandeira = []
lista_area = []
lista_cont = []
lista_pop = []
tentativas = 20
contador_cores = 0
contador_letras = 0
contador_area = 0
contador_pop = 0
contador_cont = 0
cores = dicionario_paises[pais_sorteado]['bandeira']
for cor, i in cores.items():
  if cor != 'outras' and i != 0:
    lista_cores_bandeira.append(cor)
capital = dicionario_paises[pais_sorteado]['capital']

roda_while = True

print('  =============================  \n|                               |\n|  Bem-vindo ao Insper Paises!  |\n|                               |\n  ==== Design de Software =====\n \n Comandos:\n     dica       - entra no mercado de dicas\n     desisto    - desiste da rodada\n     inventario - exibe sua posicao\n \nUm pais foi escolhido! \nTente adivinhar! \nVoce tem {0} tentativa(s) '.format(tentativas))

while roda_while:
    
    resposta = input('Qual o seu palpite?: ')

    # ACERTAR O PAIS

    if resposta.lower() == pais_sorteado:
        print('Parabens! Voce acertou em {} tentativa(s)'.format(20-tentativas+1))
        roda_while = False

    # DESISTIR

    elif resposta == 'desisto':
            certeza = input('Tem certeza que deseja desistir da rodada? [s|n]')
            if certeza == 's':
                roda_while = False
                print('Que deselegante desistir, o pais era: {}'.format(pais_sorteado))
                print('Ate a proxima!')

    #ACABAR AS TENTATIVAS
        
    elif tentativas == 1:
        print('Voce perdeu, o pais era: {}'.format(pais_sorteado))
        roda_while = False

    # DICAS

    elif resposta == 'dica':
        print(mercado_dicas(tentativas, contador_pop, capital, contador_cores, contador_letras, lista_cores_bandeira, contador_area, contador_cont ))
        opcao = int(input('Escolha sua opcao [0|1|2|3|4|5]: '))

        if opcao == 0:
            inventario = tabela_distancias(lista_inventario)
            print('\nInventario :\n {}'.format(inventario))
            print('0')

        elif opcao == 2 and contador_cores != len(lista_cores_bandeira):
            tentativas -= 4
            contador_cores += 1
            cor_sorteada = choice(lista_cores_bandeira)
            if len(lista_cores) == 0:
              lista_cores = ['Cores da bandeira', cor_sorteada]

            elif cor_sorteada not in lista_cores:
              lista_cores.append(cor_sorteada)
            lista_cores_bandeira.remove(cor_sorteada)
            print(lista_cores)

        elif opcao == 1 and contador_letras != len(capital):
            contador_letras += 1
            tentativas -= 3
            letra_sorteada = sorteia_letra(capital, lista_letras_usadas)
            if lista_letras == []:
                lista_letras = ['Letras da capital', letra_sorteada]
            else:
                lista_letras.append(letra_sorteada)
            lista_letras_usadas.append(letra_sorteada)
            print(lista_letras)
            
            

        elif opcao == 4 and contador_area != 1:
            contador_area += 1
            tentativas -= 6
            area = dicionario_paises[pais_sorteado]['area']
            lista_area = ['Area', area]
            print(lista_area)

        elif opcao == 3 and contador_pop != 1:
            contador_pop += 1
            tentativas -= 5
            populacao = dicionario_paises[pais_sorteado]['populacao']
            lista_pop = ['Populacao', populacao]
            print(lista_pop)

        elif opcao == 5 and contador_cont != 1:
            contador_cont += 1
            tentativas -= 7
            cont = dicionario_paises[pais_sorteado]['continente']
            lista_cont = ['Continente', cont]
            print(lista_cont)

        print('Você tem {} tentativa(s)'.format(tentativas))

    # INVENTARIO

    elif resposta == 'inventario':
        inventario = tabela_distancias(lista_inventario)
        print('\nInventario :\n {}'.format(inventario))

    # PAIS JA FOI INSERINDO
    
    elif resposta.lower() in dicionario_paises:

        lat1 = dicionario_paises[resposta.lower()]['geo']['latitude']
        long1 = dicionario_paises[resposta.lower()]['geo']['longitude'] 
        lat2 = dicionario_paises[pais_sorteado]['geo']['latitude']
        long2 = dicionario_paises[pais_sorteado]['geo']['longitude']
        distancia = haversine(raio_Terra, lat1, long1, lat2, long2)
        distancia = int(distancia)

        if resposta.lower() in lista_paises:
            inventario = tabela_distancias(lista_inventario)
            print('\nInventario :\n {}'.format(inventario))
            print('Este pais ja foi inserido! Insira um novo')
            print('Você tem {} tentativa(s)'.format(tentativas))
            
        else:
            lista_paises.append(resposta.lower())
            tentativas -= 1
            lista_inventario = adiciona_em_ordem(resposta.lower(), distancia, lista_inventario)
            inventario = tabela_distancias(lista_inventario)
            print('\nInventario :\n {}'.format(inventario))
            print('Você tem {} tentativa(s)'.format(tentativas))

    else:
        print('País desconhecido')
        
