#------------tarea 6 analizis de algoritmos segundo parcial-------------------
#------------Autor: Kevin Nick Rodriguez Torres-----------------------
import math
import random
class Node:
    '''
    esta es una classe que re presenta la estructura de un nodo simple con un apuntador hacia el siguiente
    '''
    def __init__(self,key):
        self.Key = key
        self.Next = None

class List(Node):
    '''
    esta es la implementacion de una lista simplemente ligada con erencia de la clase nodo
    cuenta con los metodos Show(), Empty(), Linsert()
    Show(head) --> debuelve en pantalla los elementos de la lista apartir de una cabeza
    Empty(head) --> boolean
    Linsert(Head,k)
    '''
    def __init__(self,head):
        self.Head = head
    def Show(self):
        current = self.Head
        lista = ''
        while current != None:
            lista += str(current.Key)
            lista += ' '
            current = current.Next
        print(lista)
    def __Empty(self,head):
        if head is None:
            return True
        return False

    def Linsert(self, k):
        if self.Head is None:
            x = self.Head = Node(k)
            return x
        else:
            current = self.Head
            while current.Next != None:
                current = current.Next
            current.Next = Node(k)
            return self.Head

class THash(List):
    '''
    esta clase representa la estructura de una tabla hash con los metodos siguientes:
    insert(k): este metodo inserta un valor aplicando el metodo que seleciones ya sea div o mul
    hdiv(k): este metodo lo mete en un indice segun el modulo de k % m
    hmul(k): este metodo lo mete en un indice segun el producto de m (kA % 1) donde A es una constante.
    show(): este metodo imprime la tabla hash que se creo.🎁
    '''
    def __init__(self, m, h):
        self.A = 0.6180339887
        self.H = h
        self.T = [None]*m

    def __hdiv(self,k):
        return k % len(self.T)
    def __hmul(self,k):
        return math.floor(len(self.T) * ((k * self.A)%1))

    def insert(self,k):
        if self.H == 'div':
            hash = self.__hdiv(k)
            if self.T[hash] is None:
                l=List(self.T[hash])
                self.T[hash] = l.Linsert(k)
            else:
                l=List(self.T[hash])
                self.T[hash] = l.Linsert(k)
        elif self.H == 'mul':
            hash = self.__hmul(k)
            if self.T[hash] is None:
                l = List(self.T[hash])
                self.T[hash] = l.Linsert(k)
            else:
                l=List(self.T[hash])
                self.T[hash]=l.Linsert(k)
        else:
            print('verifique el metodo ha plicar no valido!!!!!')        
    def show(self):
        print('========================================================')
        for i in range(0,len(self.T)):
            print(f"-------------[ SLOT {i} ]-------------------")
            l = List(self.T[i])
            l.Show()
        print('========================================================')

H1 = THash(15,'mul')
H2 = THash(15,'div')

U = [random.randint(0,5000) for i in range(0,100)]
for i in U:
    H1.insert(i)
    H2.insert(i)

H1.show()
H2.show()