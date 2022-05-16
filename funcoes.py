import math
from random import choice

def haversine(r, e1, h1, e2, h2):
    x = (math.sin(math.radians((e2 - e1)/2)))**2
    y = math.cos(math.radians(e1))*math.cos(math.radians(e2))*(math.sin(math.radians((h2 - h1)/2)))**2
    z = math.sqrt(x+y)
    d = 2*r*math.asin(z)
    return d

def normaliza (d1):
    nd = {}
    for continente, paises in d1.items():
        for pais, caracteristicas in paises.items():
            nd[pais] = caracteristicas 
            nd[pais]['continente'] = continente
    return nd

def sorteia_pais(d1):
    lista= []
    for pais in d1:
        lista.append(pais)
    return choice(lista)

def esta_na_lista(p, l):
    for lp in l:
        if p in lp:
            return True
    return False

def sorteia_letra(s, l):
    lc = ['.', ',', '-', ';', ' ', '']
    s = s.lower()
    for e in (lc+l):
        s = s.replace(e, '')
    if len(s) == 0:
        return ''
    return choice(s)

def adiciona_em_ordem(p, d, l):
    li = [p, d]
    if li not in l:
        if l == []:
            l.append(li)
        else:
            i = 0
            while i < len(l):
                dif = li[1] - l[i][1]
                if dif < 0:
                    l.insert(i, li)
                    return l
                i += 1
            if dif > 0:
                l.append(li)
    return l

def tabela_distancias (l1):
    nl = ''
    for e in l1:
        nl += '{} km --> {}\n'.format(e[1],e[0])
    return nl

def coloca_na_lista(l, lt):
    if lt == []:
        lt.append(l)
        return lt
    else:
        i=0
        while i < len(lt):
            if lt[i][0] > l[0]:
                lt.insert(i, l)
                return lt
            i += 1


def mercado_dicas(tentativas, contador_pop, capital, contador_cores, contador_letras, lista_cores_bandeira, contador_area, contador_cont ):
    print('Mercado de Dicas')
    print('------------------------------------------')    
    print('0. Sem dica')
    if tentativas > 3 and contador_letras != len(capital):
        print('1. Letra da capital - custa 3 tentativas')
    if tentativas > 4 and contador_cores != len(lista_cores_bandeira):
        print('2. Cor da bandeira  - custa 4 tentativas')
    if tentativas > 5 and contador_pop != 1:
        print('3. População        - custa 5 tentativas')
    if tentativas > 6 and contador_area != 1:
        print('4. Área             - custa 6 tentativas')
    if tentativas > 7 and contador_cont !=1:
        print('5. Continente       - custa 7 tentativas')
    print('-------------------------------------------')
    return ''

def tabela_dica(lista_letras,lista_cores,lista_area, lista_cont, lista_pop):
    nl = ''
    if len(lista_letras) != 0: 
        a = ''
        a += lista_letras[1][0]
        i = 1
        while i< len(lista_letras[1]):
            e = lista_letras[1][i]
            a += ', {}'.format(e)
            i += 1
        nl += '  - {}: {}\n'.format(lista_letras[0], a)

    if len(lista_cores) != 0:
        a = ''
        a += lista_cores[1][0]
        i = 1
        while i< len(lista_cores[1]):
            e = lista_cores[1][i]
            a += ', {}'.format(e)
            i += 1
        nl += '  - {}: {} \n'.format(lista_cores[0], a)

    if len(lista_pop) != 0:  
        nl += '  - {}: {}\n'.format(lista_pop[0], lista_pop[1])

    if len(lista_area) != 0:  
        nl += '  - {}: {}\n'.format(lista_area[0], lista_area[1])

    if len(lista_cont) != 0:  
        nl += '  - {}: {}\n'.format(lista_cont[0], lista_cont[1])
    
    return nl

def retorna_cor(r, g, b, texto):
    return f"\033[38;2;{r};{g};{b}m{texto}\033[38;2;255;255;255m"


