class bcolors:
    perto = '\033[92m' #GREEN
    medio = '\033[93m' #YELLOW
    longe = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def tabela_distancia_colorida(l1):
    nl = ''
    for e in l1:
        if e[1] <= 2000:
            nl += ' {} km --> {}\n'.format(e[1],e[0])
            return bcolors.perto + nl + bcolors.RESET
        elif e[1] > 2000 and e[1] <= 10000:
            nl += ' {} km --> {}\n'.format(e[1],e[0])
            return bcolors.medio + nl + bcolors.RESET
        else:
            nl += ' {} km --> {}\n'.format(e[1],e[0])
            return bcolors.longe + nl + bcolors.RESET
x = tabela_distancia_colorida([['Chile', 1200]])
print(x)