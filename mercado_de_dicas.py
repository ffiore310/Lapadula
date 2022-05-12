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
