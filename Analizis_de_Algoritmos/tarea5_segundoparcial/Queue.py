#
#
class Queue():
    '''
    esta clase representa la estructura de una cola lineal con sus metodos EnQueue,DeQueue,Show,Empty y Full
    EnQueue: este metodo encola un valor int
    Dequeue: este metodo desen cola un valor de la cola
    Show: este metodo imprime los elementos dentro de la cola sin borrarlos
    Empty: este metodo evalua si la cola esta vacia o no lo esta 
    Full: este metodo debuelve si la cola esta lleno o no
    '''
    def __init__(self,sz):
        self.Q = []
        self.SZ = sz
        self.Head = 0
        self.Tail = 0

    def EnQueue(self,v):
         if self.Full():
            print('Queue full')
         else:
            self.Q.append(v)   
            self.Tail += 1
    def DeQueue(self):
        if self.Empty():
            print('Error! Empty Queue')
        else:
            Value = self.Q[self.Head]
            del self.Q[self.Head]
            self.Tail -= 1   
        return Value
    def Show(self):
        print(self.Q)
    def Empty(self):
        if self.Head == self.Tail:
             print(True)
        else:
             print(False)   
    def Full(self):
          if self.SZ == self.Tail:
            return True
          else:
            return False   

Q = Queue(5)
Q.EnQueue(1)
Q.EnQueue(2)
Q.EnQueue(3)
Q.EnQueue(4)
Q.Show()
print(f'the Queue this Empty? {Q.Empty}')
print(f'the Queue this Full? {Q.Empty}')
Q.DeQueue()
Q.Show()