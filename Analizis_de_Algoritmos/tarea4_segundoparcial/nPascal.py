#----TAREA 4 ANALIZIS DE ALGORITMOS 2021------
#----AUTOR: KEVIN NICK RODRIGUEZ TORRE-----

n = int(input())
# fila = []
# fila_nueva = []
# def pascal (n):
#     global fila
#     for i in range(1,n):
#         tamfila = len(fila)
#         fila_nueva = [1]
#         for j in range(0,tamfila-1):
#             calculo = fila[j] + fila[j+1]
#             fila_nueva.append(calculo)
#         fila_nueva.append(1)    
#         fila = fila_nueva    
#     return fila_nueva

P=lambda h:(lambda x:x+[[x+y for x,y in zip(x[-1]+[0],[0]+x[-1])]])(P(h-1))if h>1 else[[1]]
p = P(n)
print(p[n-1])
        
# print(pascal(n))    