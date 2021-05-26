# autor: kevin nick rodriguez torres
# materiad de analizis de algoritmos
#segunda tarea del primerparcial.
# 
# import matplotlib.pyplot as plt
# import matplotlib.patches as mpatches
# x = []
# y = []
# y2 = []
# proxies = []
# legend_names = ['4n','3n+8']

# for n in range(0,100):
#     x.append(n)
#     y.append(4*n)
#     y2.append((3*n)+8)

# plt.plot([8],[32],'ro')
# plt.stem(x,y2, markerfmt = "green")
# plt.stem(x, y,  markerfmt = "blue",label="4n")

# red_patch = mpatches.Patch(color='green', label='3n+8')
# red_patch2 = mpatches.Patch(color='blue',label='4n')
# plt.legend(handles=[red_patch,red_patch2])

# plt.show()

Decada = int(input())
FechaInit = int(input())
FechaFinal = int(input())

cont = 1
item = 0
initU = FechaInit % 10
finalU = FechaFinal % 10
initD = FechaInit % 100
finalD = FechaFinal % 100

x = (initD - initU)
y = (finalD - finalU)

if x == Decada:
    for i in range(initD,x+10):
        cont += 1
    FechaInit += (100 - initU)

if y == Decada:
    for i in range(y,finalD):
        cont += 1
    FechaFinal -= (100 - finalU)   

while FechaInit <= FechaFinal:
    item += 1
    FechaInit += 100   
cont += (item * 10)

print(cont)