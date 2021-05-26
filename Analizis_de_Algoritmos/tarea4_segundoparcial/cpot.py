#----TAREA 4 ANALIZIS DE ALGORITMOS 2021------
#----AUTOR: KEVIN NICK RODRIGUEZ TORRE-----

def filtrarList(a):
    '''
    esta funcion transforma el array en un array valido para el algoritmo
    filtrarList(a) ---> list valida
    a : list
    '''
    Li = []
    aux = ''
    for i in a:
        if i != ' ':
            aux += i 
        elif i == ' ' and aux != '':
            Li.append(int(aux))
            aux = ''        
    return Li     

conPot = list(input())
conPot.append(' ')#manejo de error de logica
conPot = filtrarList(conPot)


def potencia(c):
    """Calcula y devuelve el conjunto potencia del 
       conjunto c.
    """
    if len(c) == 0:
        return [[]]
    r = potencia(c[:-1])
    return r + [s + [c[-1]] for s in r]
        
print(potencia(conPot))










