# Analisis de algoritmos
# autor: kevin nick rodriguez torres
#ejercicio 2 de tarea 3 del primerparcial.

# import matplotlib.patches as mpatches
# import matplotlib.pyplot as plt
# x = []
# y = []
# y2 = []
# proxies = []
# legend_names = ['n']

# for n in range(0,10):
#     x.append(n)
#     y.append(n)

# plt.stem(x, y,  markerfmt = "blue",label="n")

# red_patch2 = mpatches.Patch(color='blue',label='n')
# plt.legend(handles=[red_patch2])

# plt.show()

# def filtrarList(a):
#     '''
#     esta funcion transforma el array en un array valido para el algoritmo
#     filtrarList(a) ---> list valida
#     a : list
#     '''
#     Li = []
#     aux = ''
#     for i in a:
#         if i != ' ':
#             aux += i 
#         elif i == ' ' and aux != '':
#             Li.append(aux)
#             aux = ''        
#     return Li  

# Lista2 = []
# Lista = list(input())
# Lista.append(' ')
# Lista = filtrarList(Lista)

# for p in Lista:
#     Lista2.append(p[::-1])

# print(Lista == Lista2)

cont = 0

for i in range(1,10):
    for j in range(1,10):
        cont += pow(2,i) * pow(2,(3*j)) 
print(cont)        