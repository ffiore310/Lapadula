
def tabela_distancia_colorida(l1):
    nl = ''
    for e in l1:
        if e[1] <= 2000:
            nl += ' {} km --> {}\n'.format(e[1],e[0])
        elif e[1] > 2000 and e[1] <= 10000:
            nl += ' {} km --> {}\n'.format(e[1],e[0])
        else:
            nl += ' {} km --> {}\n'.format(e[1],e[0])
    return nl
x = tabela_distancia_colorida([['Chile', 6000],['Botsuana', 13000]])
print(x)