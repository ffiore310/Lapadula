import math

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

