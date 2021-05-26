#----TAREA 4 ANALIZIS DE ALGORITMOS 2021------
#----AUTOR: KEVIN NICK RODRIGUEZ TORRE-----
import math
v1 = int(input())
v2 = int(input())

def karatsuba(num1,num2):
    '''
    ESTA FUNCION ES RECURSIVA Y CALCULA EL PRODUCTO DE DOS NUMEROS DE TAMAÑO N
    KARATSUBA(NUM1,NUM2) ---> EL PRODUCTO
    NUM1: NUMERO ENTERO POSITIVO
    NUM2: NUMERO ENTERO POSITIVO
    '''
    if num1 < 10 and num2 < 10:
        return num1 * num2
    else:
        m = max(len(str(num1)),len(str(num2)))
        m2 = math.floor(m / 2)

        a = math.floor(num1 / pow(10,m2))
        b = num1 % pow(10,m2) 
        c = math.floor(num2 / pow(10,m2))
        d = num2 % pow(10,m2)

        p1 = karatsuba(a,c)
        p2 = karatsuba(b,d)
        p3 = karatsuba((a+b),(c+d))
        p4 = (p3-p2-p1)
        if p4 < 0:
            p4 *= -1
        return (p1 * math.pow(10,(2*m2))) + p2 + (p4 * (pow(10,m2)))
        
print(karatsuba(v1,v2))      
