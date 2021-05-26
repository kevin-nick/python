#----TAREA 4 ANALIZIS DE ALGORITMOS 2021------
#----AUTOR: KEVIN NICK RODRIGUEZ TORRE-----

import os

vocal = 0
consonante = 0

# def txt_rel(nomarch):
#     """
#     esta funcion recive el nomarch de un archivo .txt para comprobar si existen mas vocales que consonantes en el archivo
#     txt_rel(nomarch) ---> lectura del nomarch o #f si el archivo no existe
#     nomarch: string
#     """
#     global vocal
#     global consonante
#     if os.path.isfile(nomarch):
#         archivo = open(nomarch, 'r')
#         linea = archivo.read(1)
#         while linea != "":
#                linea = archivo.read(1)
#                if linea in "aeiou" or linea in "AEIOU":
#                    vocal += 1
#                if linea in "bcdfghjklmnñpqrstvwxyz" or linea in "BCDFGHJKLMNÑPQRSTVWXYZ":
#                    consonante += 1   
#         archivo.close()  
#     else:
#         print('#f; el archivo no existe')

# txt_rel('tx.txt')

tx = list(input())
if len(tx) == 0:
    print('ingresa una cadena de caracteres!')
    
def AnalizadorTx(tx):
    '''
    esta funcion recursiva analiza uba lista de caracteres tecledas desde consola diciendo si hay mas vocales que constantes
    AnalizadorTx(tx) ---> boolean
    tx: string
    '''
    global vocal
    global consonante

    if len(tx) == 0:
        return
    else:
        linea = tx.pop()    
        if linea in "aeiou" or linea in "AEIOU":
            vocal += 1
            return AnalizadorTx(tx)
        if linea in "bcdfghjklmnñpqrstvwxyz" or linea in "BCDFGHJKLMNÑPQRSTVWXYZ":
            consonante += 1   
            return AnalizadorTx(tx)

AnalizadorTx(tx)

if vocal >= consonante:
    print(True)
else:
    print(False)    