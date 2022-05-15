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
    lc = ['.', ',', '-', ';', ' ']
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


tabela_ini_dicas = [ 
[0, '0. Sem dicas'],
[1, '1. Cor da bandeira  - custa 4 tentativas'],
[2, '2. Letra da capital - custa 3 tentativas'],
[3, '3. Área             - custa 6 tentativas'],
[4, '4. População        - custa 5 tentativas'],
[5, '5. Continente       - custa 7 tentativas'],
]

dicas_ja = []
opcao = int(input('opcao'))
def tabela_dicas(dicas_ja, opcao):
    if opcao not in dicas_ja and opcao > 2:
        dicas_ja.append(opcao)
        for e in tabela_ini_dicas:
            print (e[1])
    elif opcao in dicas_ja and opcao >2:
        tabela_ini_dicas[opcao][1] = ''
        for e in tabela_ini_dicas:
            print (e[1])
    
tabela_dicas(tabela_ini_dicas, opcao)

    