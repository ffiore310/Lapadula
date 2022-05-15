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
        nl += ' {} km --> {}\n'.format(e[1],e[0])
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

# l1 = {dicas01:valor, dica02:valor02 }
def tabela_dicas (l1):
    nl = ''
    for k,v in l1.items():
        nl += '- {}: {}\n'.format(k,v)
    return nl



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
    if tentativas> 6 and contador_area != 1:
        print('4. Área             - custa 6 tentativas')
    if tentativas > 7 and contador_cont !=1:
        print('5. Continente       - custa 7 tentativas')
    print('-------------------------------------------')
    return ''



 
