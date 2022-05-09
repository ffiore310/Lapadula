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