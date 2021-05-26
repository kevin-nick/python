#
#

class Stack():
    '''
    esta es una class que representa el funcionamiento de una pila de estructura
    con tiene los metodos push, pop,show y Stack_Empty.
    Push: ingresa un valor a la pila
    Pop: extrae un numero de la pila
    Stack_Empty: determina si la pila esta vacia o no
    Show: imprime los valores de la pila sin eliminarlos o extraerlos
    '''

    def __init__(self,sz):
       self.S = [] 
       self.top = 0
       self.SZ = sz
    def show(self):
        if self.Stack_empty():
            print('Empty Stack')
        else:
            c = []
            for i in self.S:
                if i != '':
                    c.append(i)
            print(c)        
    def Stack_empty(self):  
        if self.top == 0:
          return True
        else:
          return False  

    def Pop(self):
        if self.top == 0:
            print('Error! Empty Stack')
        else:
            self.S[self.top-1] = ''
            self.top -= 1    

    def Push(self,v):
        if self.top == self.SZ:
            print('Stack full')
        else:
            self.S.append(v)   
            self.top += 1

s = Stack(10)
s.Push(10)
s.Push(1)
s.Push(13)
s.Push(13)
s.Push(13)
s.Push(13)
s.Push(13)
s.Push(13)
s.Push(13)
s.show()
s.Pop()
s.show()
s.Push(13)
s.Push(13)
s.show()
s.Push(13)
