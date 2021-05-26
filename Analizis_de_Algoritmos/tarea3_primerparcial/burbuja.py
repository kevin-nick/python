# Analisis de algoritmos
# autor: kevin nick rodriguez torres
#ejercicio 1 de tarea 3 del primerparcial.

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
Array = filtrarList(Array) #convercion de lista a lista valida
Li = len(Array)
i = 0

while i < Li: #primera iterante
      j = i
      while j < Li: #segunda iterante
              if Array[i] > Array[j]: #verificacion para hacer cambio de valor
                      aux = Array[i]
                      Array[i] = Array[j]
                      Array[j] = aux
              j += 1
      i += 1 

print(Array)


