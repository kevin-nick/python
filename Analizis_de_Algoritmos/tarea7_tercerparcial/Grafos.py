# tarea 7 analizis de algoritmos ujat.
#autor: Kevin Nick Rodriguez Torres.

from graphviz import Digraph
import os

class Vertices:
    '''
    esta clase reprecenta los vertices su key y su adyacencias
    '''
    def __init__(self,key ,ady = [],view = False):
        self.key = key
        self.ady = ady
        self.view = view 

class Aristas():
    '''
    esta clase representa las aritas que conectan los vertices
    '''
    def __init__(self,vi,vf,ew = None):
        self.vi = vi
        self.vf = vf    
        self.A = [vi.key,vf.key]  
        self.ew = ew

class Grafo():
    '''
    esta clase genera grafos a partir de vertices y aristas
    '''
    def __init__(self,V,A,dir = True,nombre = 'G'): #constructor
        self.V = V
        self.A = A
        self.dir = dir
        self.nombre = nombre

    def __Adj(self):
        '''
        metodo privado de la clase grafo este metodo crea lista de adyacencia
        self.__Adj ---> lista de abjacencia
        '''
        ListA = []
        AuxL = []
        aux = 0;
        for i in self.V:
            AuxL.append(i.key)
            for j in self.A:
                if j.A[0] == i.key:
                    AuxL.append(j.A[1])
            ListA.append(AuxL)
            AuxL = []
        print(ListA)

    def __MA(self):  
        '''
        metodo privado de la clase grafo el  cual genera una matriz de adjacencia
        self.___MA() ---> matriz de abjacencia
        '''
        MatrizAdj = [[0] * len(self.V) for i in range(len(self.V))] 
        for i in self.V:
            for j in self.A:
                if j.A[0] == i.key:
                    MatrizAdj[i.key - 1][j.A[1] - 1] = 1
        print(MatrizAdj)            

    def Adj(self):
        'metodo publico de la clase grafo invoca a su analogo privado'
        self.__Adj()

    def Ma(self):
        'metodo publico de la clase grafo invoca a su analogo privado'
        self.__MA()

    def Inf(self):
        '''
        metodo de la clase grafo el cual debuelve la informacion del grafo
        grafo.Inf() ---> vertices y aristas
        '''
        vertice = []
        Ar = ''
        for i in self.V:
            vertice.append(i.key)
        print('V = '+str(vertice))
        for i in self.A:
            Ar += str(i.A) 
        print('A = {'+Ar+'}')

    def Show(self):
        '''
        metodo de la clase grafo que genera un .dot para ser visualizado como png
        '''
        dot = Digraph()
        for i in self.V:
            dot.node(str(i.key), str(i.key),shape= 'circule')
        for i in self.A:
            dot.edge(str(i.A[0]),str(i.A[1]))
        dot.render(filename=self.nombre+'.dot', directory=r'c:\User\NICK\Desktop', view=True, format='png')
        # os.system(r'dot -Tpng c:\User\NICK\Desktop\grafo.dot -o img.png')

v1 = Vertices(1)
v2 = Vertices(2)
v3 = Vertices(3)
v4 = Vertices(4)
v5 = Vertices(5)
v6 = Vertices(6)

A1 = Aristas(v1,v2)
A2 = Aristas(v3,v4)
A3 = Aristas(v1,v3)
A4 = Aristas(v3,v2)
A5 = Aristas(v4,v1)
A6 = Aristas(v5,v1)
A7 = Aristas(v4,v6)
A8 = Aristas(v6,v5)
A9 = Aristas(v1,v6)
A10 = Aristas(v2,v4)
A11 = Aristas(v4,v5)

g = Grafo([v1,v2,v3,v4,v5,v6],[A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11],True)
g.Inf()
g.Adj()
g.Ma()
# g.Show()