#----TAREA 4 ANALIZIS DE ALGORITMOS 2021------
#----AUTOR: KEVIN NICK RODRIGUEZ TORRE-----
#  
import math
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

Array = list(input()) #ingreso de datos
Array.append(' ') #manejo de error de logica
Clave = int(input())

def BusBinaria (Array,Clave):
    Alto = len(Array)   
    central = math.floor(Alto / 2)  #Dividir

    if Array[central] == Clave: #Vencer
        print(True)
        return
    if len(Array) < 2:
        print(False)
        return    
    elif Array[central] < Clave:  #Dividir
        BusBinaria(Array[central:Alto],Clave) #Combinar
    elif Array[central] > Clave:  #Dividir
        BusBinaria(Array[0:central],Clave) #Combinar

if Array != [" "]:
    Array = filtrarList(Array) #filtra el array en valores validos
    BusBinaria(Array,Clave)
else:
    print(False)