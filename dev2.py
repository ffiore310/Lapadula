from termcolor import colored

tabela_ini_dicas = [ 
[0, ' Sem dicas'],
[1, ' Cor da bandeira  - custa 4 tentativas'],
[2, ' Letra da capital - custa 3 tentativas'],
[3, ' Área             - custa 6 tentativas'],
[4, ' População        - custa 5 tentativas'],
[5, ' Continente       - custa 7 tentativas'],
]

dicas_ja = []
while True:

    opcao = int(input('opcao: '))

    def tabela_dicas(dicas_ja, opcao, tabela_ini_dicas):

        if opcao not in dicas_ja and opcao > 2:
            dicas_ja.append(opcao)
            i = 0
            for e in tabela_ini_dicas:
                print ('{}. {}'.format(i, e[1]))
                i+=1
        elif opcao in dicas_ja and opcao >2:
            tabela_ini_dicas[opcao][1] = ''
            for e in tabela_ini_dicas:
                print (e[1])
        return ''
        
    print(tabela_dicas(dicas_ja, opcao, tabela_ini_dicas))

























# MERCADO DE DICA

dicas = {}
print('Mercado de Dicas \n ------------------------------------------\n 0. Sem dica\n 1. Cor da bandeira    - custa 4 tentativas\n 2. Letra da capital   - custa 3 tentativas\n 3. Area               - custa 6 tentativas\n 4. Populacao          - custa 5 tentativas\n 5. Continente         - custa 7 tentativas\n ------------------------------------------')
opcao = int(input('Escolha sua opcao [0|1|2|3|4|5]: '))

if opcao == 0:
    inventario = tabela_distancias(lista_inventario)
    print(inventario)
    # = 


elif opcao == 1:
    print('fernando')

elif opcao == 2:
    print('humberto')

elif opcao == 3:
    for e, i in dicionario_paises.items():
        area = i['area']
        dicas['Área'] = area
        print('dicas')
    

elif opcao == 4:
    print('jose')

else:
    print('A')