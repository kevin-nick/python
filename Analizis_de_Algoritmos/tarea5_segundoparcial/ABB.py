#
#

class Nodo:
    def __init__(self, dato):
        # "dato" puede ser de cualquier tipo, incluso un objeto si se sobrescriben los operadores de comparación
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class Arbol(Nodo):
    # Funciones privadas
    def __init__(self, dato):
        self.raiz = Nodo(dato)

    def __Insert(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self.__Insert(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.__Insert(nodo.derecha, dato)

    def __Inorder_Walk(self, nodo):
        if nodo is not None:
            self.__Inorder_Walk(nodo.izquierda)
            print(nodo.dato, end=", ")
            self.__Inorder_Walk(nodo.derecha)

    def __Search(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.dato == busqueda:
            return nodo
        if busqueda < nodo.dato:
            return self.__Search(nodo.izquierda, busqueda)
        else:
            return self.__Search(nodo.derecha, busqueda)

    def __Minimum(self,nodo):
        if nodo.izquierda is None:
           print(f'el nodo minimo es: {nodo.dato}')
           return nodo
        else:
            self.__Minimum(nodo.izquierda)    

    def __Maximum(self,nodo):
        if nodo.derecha is None:
            print(f'el nodo maximo es: {nodo.dato}')
        else:
            self.__Maximum(nodo.derecha)  

    def __Sucesor(self,nodo):
        x = self.__Search(self.raiz,nodo)
        izq = x.izquierda
        der = x.derecha
        if izq != None and der != None:
            print(f'{izq.dato} <| {x.dato} |> {der.dato}')
        elif izq != None :
            print(f'{izq.dato} <| {x.dato} |> {der}')
        elif der != None:
            print(f'{izq} <| {x.dato} |> {der.dato}')    
        else:
            print(f'{izq} <| {x.dato} |> {der}')

    def __Predecessor(self,nodo,busqueda):
        if nodo is None or busqueda is None:
            print('no existe')    
            return

        left = nodo.izquierda
        right = nodo.derecha    

        if left != None:
            if busqueda == left.dato:
                print(f'el padre de {busqueda} es: {nodo.dato}')
                return nodo
        if right != None:
            if busqueda == right.dato:
                print(f'el padre de {busqueda} es: {nodo.dato}')
                return nodo
        if  busqueda < nodo.dato:
            return self.__Predecessor(nodo.izquierda, busqueda)
        else:
            return self.__Predecessor(nodo.derecha,busqueda)

    def __Transplant(self,T,nodo,value):
        if T == None:
            T = value
        elif nodo == T.izquierda:
            T.izquierda = value
        else:
            T.derecha = value
        if value != None:
           u = T

         
    def __Delete(self,nodo):
        if nodo.izquierda == None:
            self.__Transplant(self.__Predecessor(self.raiz,nodo),nodo,nodo.derecha)
        if nodo.derecha == None:
            self.__Transplant(self.__Predecessor(self.raiz,nodo),nodo,nodo.izquierda)
        else:
            n = self.__Minimum(nodo.derecha)
            if self.__Predecessor(self.raiz,n) != nodo:
                This.__Transplant(self.__Predecessor(self.raiz,n),n,n.derecha)
                n.derecha = nodo.derecha
                np = self.__Predecessor(self.raiz,n)
                np.derecha = n
            self.__Trasplant(self.__Predecessor(self.raiz,nodo),nodo,n) 
            n.izquierda = nodo.izquierda
            np.derecha = n
    # Funciones públicas

    def agregar(self, dato):
        self.__Insert(self.raiz, dato)

    def inorden(self):
        print("Imprimiendo árbol inorden: ")
        self.__Inorder_Walk(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self.__Search(self.raiz, busqueda)

    def nodominimo(self):
        self.__Minimum(self.raiz)   
    def nodomaximo(self):
        self.__Maximum(self.raiz) 

    def Sucesor(self,nodo):
        self.__Sucesor(nodo)        

    def Predecesor(self,nodo):
        self.__Predecessor(self.raiz,nodo)

    def Delete(self,nodo):
        x = self.__Search(self.raiz,nodo)
        self.__Delete(x)

arbol = Arbol(18)
arbol.agregar(12)
arbol.agregar(10)
arbol.agregar(7)
arbol.agregar(4)
arbol.agregar(5)
arbol.agregar(2)
arbol.agregar(21)
arbol.inorden()
arbol.nodominimo()
arbol.nodomaximo()
#Búsqueda
busqueda = int(input("Busca algo en el árbol: "))
nodo = arbol.buscar(busqueda)
if nodo is None:
    print(f"{busqueda} no existe")
else:
    print(f"{busqueda} sí existe")
    # Aquí tienes en "nodo" toda la información del nodo. Tanto su izquierda, derecha, dato y otros atributos que le hayas agregado
arbol.Sucesor(4)
arbol.Predecesor(7)
arbol.Delete(4)
