#----TAREA 4 ANALIZIS DE ALGORITMOS 2021------
#----AUTOR: KEVIN NICK RODRIGUEZ TORRE-----

base = int(input())
exponente = int(input())
res = 1
def cuad(baux,base,NewExpo):
    '''
    ESTA FUNCION CALCULA EL EXPONENTE DE UN NUMERO A UNA POTENCIA DADA RECURSIVAMENTE
    CUAD(BAUX,BASE,NEWEXPO) ----> NUMBER
    BAUX: NUMBER POSITIVO
    BASE: NUMBRE POSITIVO
    NEWEXPO: NUMBER POSITIVO
    '''
    if NewExpo == 1:
        return base
    else:
        return cuad(baux,baux*base,NewExpo-1)    


if exponente == 0:
    print(res)  
    exit()
elif exponente % 2 == 0:
    NewExpo = int(exponente/2)
    baux = base
    res = cuad(baux,base,NewExpo) 
    res *= res
else:
    baux = base
    res = base * cuad(baux,base,exponente-1)   

print(res)    