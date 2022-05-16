from cgitb import reset


RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
def tabela_distancia_colorida(l1):
    nl = ''
    for e in l1:
        if e[1] <= 2000:
            nl += GREEN +'{}'+ reset + 'km --> {}\n'.format(e[1],e[0])
        elif e[1] < 10000 and e[1]>2000:
            nl += YELLOW +'{}'+ reset + 'km --> {}\n'.format(e[1],e[0])
        else:
            nl += RED +'{}'+ reset + 'km --> {}\n'.format(e[1],e[0])
    return nl
x = tabela_distancia_colorida([['Chile', 6600], ['Russia', 12000], ['Nigeria', 1200]])