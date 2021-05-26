# Analisis de algoritmos
# autor: Kevin nick rodriguez torres
#ejercicio 2 de tarea 1 del parcial 1

x = float(input())
y = float(input())
z = float(input())

res = ((((2 * x) + y) / z) * (pow(y , 3) - z)) / (((x + (2 * y) + (3 * z)) / (z - (2 * y) - (3 * x))) + pow(x , 2) + pow(z , 2))

print(f"resultado: {res}")