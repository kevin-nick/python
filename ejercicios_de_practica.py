def cvacio(A):
    """
    esta funcio evalua si el conjunto dado es vacio o no retornando un valor bool
    cvacio(A) --> bool
    A : conjunto
    """
    if A == {}:
       return True
    return False  
# print(cvacio(B))
# print(cvacio(c))
# ---------------------------------------fin--------------------------------------------------------------------------
#B = {1,2,3}
def en(e,A):
    """
    esta funcion recive un elemento y un conjunto y retorna un valor bool
    en(e,A) --> bool
    e : elemento    
    A : onjunto
    """
    return e in A
#print(en(3,B))    
#----------------------------------------fin---------------------------------------------------------------------------
#B = {1, 2 , 3,'a',"hola",}
def card(A):
    """
    esta funcion recive un conjunto y retorna la cardinalidad del mismo
    card(A) --> un numero
    A : conjunto
    """
    return len(A)
#print(card(B))
#------------------------------------------fin-------------------------------------------------------------------------
def subc(A,B):
    """
    esta funcion recive dos conjuntos y debuelve un valor bool
    subc(A,B) --> bool 
    A : conjunto             
    B : conjunto
    """
    if A == {}:
        return True
    return A.issubset(B)

#print(subc(C,D))   
#------------------------------------------------------fin-------------------------------------------------------------
def igual(A,B):
    """
    esta funcion recibe dos conjuntos A y B y debuelve un valor bool.
    igual(A,B) --> bool
    A : conjunto   
    B : conjunto
    """
    return A == B
help(igual)     
#print(igual(C,D))    
#-------------------------------------fin------------------------------------------------------------------------------
res = set()
res = {}
def UnionG(lc):  
    """
    esta funcion recibe una lista de n conjunto y debuelve un conjunto.
    UnionG([A,B,C...]) --> conjunto 
    [A1;A2; : : : ;An]. ---> lista de conjuntos
    """
    res = lc[0]
    for x in range(0,len(lc)):
        res = res | lc[x]
    return res    
#print(UnionG([{1,2,3},{4,5,6},{7,8,9},{10},{'a'}]))
#--------------------------------------------------------fin-----------------------------------------------------------
res = set()
res = {}
def IntersecG(lc):
    """
    esta funcion recibe una lista de n conjunto y debuelve un conjunto
    IntersecG([A,B,C...]) ---> conjunto 
    [A1;A2; : : : ;An]. ---> lista de conjuntos
    """
    res = lc[0]
    for x in range(0,len(lc)):
        res = res & lc[x]
    return res   
#print(IntersecG([{1,2,3,'a'},{1 , 2 ,5,'b'},{2,'a', 3},{'a',2}]))
#---------------------------------------------------------fin----------------------------------------------------------

def difsim(A,B):
    """
    esta funcion recive 2 conjuntos y retorna la diferencia simetria de ambos conjuntos.
    difsim(A,B) --->  un conjunto con la diferencia simetria
    A : conjunto 
    B : conjunto
    """
    return A ^ B    
#print(difsim({1,2,3,4,5},{1,2,3,5,6,7,9}))
#------------------------------------------FIN-------------------------------------------------------------------------

def cub(F,A):
    """
    esta funcion determina si una familia de conjuntos es un cubrimiento de un conjunto dado
    cub(F,A) ---> boolean
    F: familia de conjuntos 
    A: conjunto 
    """
    u = UnionG(F)
    return A.issubset(u)
#print(cub([{1,2,3,'a'},{1, 2 ,5,'a'},{2,'a', 3},{'a',2}],{1,2,3}))
#--------------------------------------------FIN-----------------------------------------------------------------------

def part(F,A):
    """
    esta funcion determina si una familia de conjuntos es particion de un conjunto
    part(F,A) ---> boolean
    F: familia de conjuntos 
    A: conjunto 
    """ 
    aux = 0
    if cub(F,A):
        for x in F:
            aux += 1
            for v in range(aux,len(F)):
                if x.isdisjoint(F[v]):
                    continue
                else:
                    return False   
        return True        
    else:
        return False    
#print(part([{1,2,3,'a'},{0, 4 ,5},{6,7,8,'b'},{'c',11,9}],{1,'a',3}))
#--------------------------------------------FIN------------------------------------------------------------------------
import os
def txt_rel(nomarch):
    """
    esta funcion recive el nomarch de un archivo .txt para comprobar dicha existencia y posterior mente abrirlo
    txt_rel(nomarch) ---> lectura del nomarch o #f si el archivo no existe
    nomarch: string
    """
    relf = []
    if os.path.isfile(nomarch):
        archivo = open(nomarch, 'r')
        for linea in archivo:
               relf.append(linea)    
        archivo.close()  
    else:
        print('#f ; el archivo no existe')
    return relf      
#print(txt_rel("CF.txt"))
#----------------------------------------------FIN----------------------------------------------------------------------

def Im(R,a):
    """
    esta fun cion recibe una lista de relaiones y un elemento evaluando al elemento y devolviendo un conjunto con sus imagenes
    Im(R,a) ---> conjunto
    R: relacion
    a: elemento
    """
    res = set()
    for x in R:
        aux = x.pop(0)
        if aux == a:
            res.add(x.pop())
    return res
#print(Im([['a',1],['a',3],['b',2]],'a'))
#-------------------------------------------------------FIN-------------------------------------------------------------

def ref(R,D=None):
    """
    esta funcion determina si una relacion es reflexiva 
    ref(R,D) ---> boolean
    R: relacion
    D: dominio (opcional) 
    """
    lista = []
    cont = 0
    if D == None:
        for r in R:
            aux = r.pop(0)
            lista.append(aux)
            aux2 = r.pop()
            if aux == aux2:
                cont += 1  
        if len(set(lista)) == cont:
            return True
        else:
            return False    
    else:
        for r in R:
            aux = r.pop(0)
            aux2 = r.pop()
            if aux == aux2:
                cont += 1  
        if len(D) == cont:
            return True
        else:
            return False  
#print(ref([['a',1],['a',2],['a','a'],['b',3],['b','b']],['a','b']))
#--------------------------------------------------FIN------------------------------------------------------------------

def irref(R,D=None):
     """
      esta funcion determina si una relacion es irreflexiva 
      ref(R,D) ---> boolean
      R: relacion
      D: dominio (opcional) 
     """
     if D == None:
        for r in R:
            aux = r.pop(0)
            aux2 = r.pop()
            if aux == aux2:
                return False
        return True           
     else:
        for r in R:
            aux = r.pop(0)
            aux2 = r.pop()
            if aux == aux2:
                return False
        return True         
#print(irref([['a',1],['a',2],['a','z'],['b',3],['b','z']]))
#----------------------------------------------------FIN----------------------------------------------------------------
lista = []
lista2 = []
def dom(R):
    for r in R:
        lista.append(r[0])
    return lista   
def ran(R):
     for r in R:
         lista2.append(r[1])
     return lista2     
#----------------------------------------------------------------------------------------------------------------------
def sim(R,D=None):
    """
    esta es una funcion determina si una relacion es simetrica
    sim(R,D) ---> boolean
    R: relacion
    D: dominio(opcional)
    """
    a = []
    b = []
    f1 = []
    if D == None:
        a = dom(R)
        b = ran(R)
        for i in range(len(R)):
            f1.append(a[i])
            f1.append(b[i])
            if f1 in R:
                f1.clear()
                f1.append(b[i])
                f1.append(a[i])
                if f1 in R:
                    f1.clear()
                    continue
                else:
                    return False    
        return True                    
    else:
        a = dom(R)
        b = ran(R)
        for i in range(len(R)):
            f1.append(a[i])
            f1.append(b[i])
            if f1 in R:
                f1.clear()
                f1.append(b[i])
                f1.append(a[i])
                if f1 in R:
                    f1.clear()
                    continue
                else:
                    return False    
        return True                  
#print(sim([[1,2],[2,1],[3,2],[2,3],[1,1]],[1,2,3]))
#------------------------------------------------FIN-------------------------------------------------------------------

def asim(R,D=None):
    """
    esta es una funcion determina si una relacion es asimetrica
    asim(R,D) ---> boolean
    R: relacion
    D: dominio(opcional)
    """
    a = []
    b = []
    f1 = []
    if D == None:
        a = dom(R)
        b = ran(R)
        for i in range(len(R)):
            f1.append(a[i])
            f1.append(b[i])
            if f1 in R:
                f1.clear()
                f1.append(b[i])
                f1.append(a[i])
                if f1 in R:
                   return False 
                else:
                    f1.clear()
                    continue                  
        return True                    
    else:
        a = dom(R)
        b = ran(R)
        for i in range(len(R)):
            f1.append(a[i])
            f1.append(b[i])
            if f1 in R:
                f1.clear()
                f1.append(b[i])
                f1.append(a[i])
                if f1 in R:
                    return False  
                else:
                    f1.clear()
                    continue                     
        return True                  
#print(asim([[1,2],[2,3],[4,2],[1,3],[1,0]],[1,2,4]))
#-----------------------------------------------FIN--------------------------------------------------------------------

def antsim(R,D=None):
    """
    esta es una funcion qeu debuelve la antisimetria de una relacion evaluando su relacion
    antsim(R,D) ---> boolean
    R: relacion
    D: dominio (opcional)
    """
    a = []
    b = []
    if D == None:
        if asim(R):
            return False
        else:
            a = dom(R)
            b = ran(R)
            for i in range(len(R)):
                if a[i] != b[i]:
                    return False
            return True           
    else:
        if asim(R):
            return False
        else:
            a = dom(R)
            b = ran(R)
            for i in range(len(R)):
                if a[i] != b[i]:
                    return False
            return True            
#print(antsim([[2,2],[4,4]],[1,2]))
#------------------------------------------FIN-------------------------------------------------------------------------

def trans(R,D=None):
    """
    esta funcion retorna si una relacion es transitiva o no lo es evaluando una lista de pares
    trans(R,D) ---> boolean
    R: relacion
    D: dominio (opcional)
    """
    a = []
    b = []
    nlis = []
    if D == None:
        a = dom(R)
        b = ran(R)
        for i in range(len(R)):
            if a[i] == b[i]:
                continue
            else:
                for x in range(i,len(R)):
                    if b[i] == a[x]:
                       nlis.append(a[i])
                       nlis.append(b[x])
                       if nlis in R:
                           continue
                       else:
                           return False
        return True      
    else:
        a = dom(R)
        b = ran(R)
        for i in range(len(R)):
            if a[i] == b[i]:
                continue
            else:
                for x in range(i,len(R)):
                    if b[i] == a[x]:
                       nlis.append(a[i])
                       nlis.append(b[x])
                       if nlis in R:
                           continue
                       else:
                           return False
        return True      
#print(trans([['a','a'],['b','b'],['c','c'],['d','d'],['e','e'],['b','c'],['b','a']]))               
#----------------------------------------------FIN----------------------------------------------------------------------

def fun(R,D=None):
    """
    esta funcion recibe un conjunto de pares y evalua si es una funcion o no lo es 
    fun(R,D) ---> boolean
    R: relacion
    D: dominio(opcional)
    """
    a = []
    if D == None:
          a=dom(R)
          for i in a:
            if a.count(i) > 1:
                return False
          return True
    else:
        a = dom(R)
        if len(a) == len(D):
            for i in a:
                if D.count(i) > 1 or i not in D:
                    return False
            return True 
        else:
            return False              
#print(fun([[1, 'w'],[2, 'x'],[3, 'x']],[1,2,3]))    
#------------------------------------------FIN--------------------------------------------------------------------------

def Ran(f):
    """
    esta funcion debuelve el rango de una funcion apartir de un conjunto de pares f
    Ran(f)  ---> Rango
    f: conjunto de pares ordenados
    """
    for r in f:
         lista2.append(r[1])
    return lista2 
#print(Ran([[1, 'w'],[2, 'x'],[3, 'x']]))   
#----------------------------------------------FIN----------------------------------------------------------------------

A = {12,13}
B = {2,4,6,8}
res = set()
res = {}
def procart(A,B):
    """
    esta funcion debuelve el producto cartesiano de dos conjuntos
    procart(A,B) ---> lista de conjuntos
    A: conjunto
    B es un conjunto
    """
    return {(a,b)for a in A for b in B}    
#print(procart(A,B))
#------------------------------------------------------------------------------------
def subalf(S1,S2):
    """
     esta funcion determina si S1 es un sub alfabeto de S2
     subalf(S1,S2) ---> boolean
     S1: alfabeto
     S2: alfabeto
    """
    if S1 != []:
        if S1.pop() in S2:
            subalf(S1,S2)
        else:
            return False   
    return True    
#print(subalf([1,2,3,4,5],[2,4,5]))  
#----------------------------------------FIN---------------------------------------------------

def subalfp(S1,S2):
    """
     esta funcion determina si S1 es un sub alfabeto propio de S2
     subalfp(S1,S2) ---> boolean
     S1: alfabeto
     S2: alfabeto
    """ 
    if S1 != []:
        if S1.pop() in S2:
            subalf(S1,S2)
        else:
            return True  
    return False  
#print(subalfp([],[]))
# ---------------------------------------------------------FIN------------------------------------------ 
def simbolo(w):
    """
     recibe una lista y debuelve si es un simbolo o no sus elementos de la lista
     simbolo(w) ---> boolean
     w: lista 
    """
    for s in w:
        if isinstance(s, str):
            continue
        elif isinstance(s, int):
            continue
        elif isinstance(s, bool):
            continue    
        else:
            return False
    return True        
#--------------------------------------Fin_--------------------------------------------------------------------
def es_pal(w):   #<<<<<----------------------------------------------
    """
    esta funcion recibe un parametro y regresa si es o no es palabra
    es_pal(w) ---> boolean
    w: parametro
    """
    return  isinstance(w, list) and simbolo(w)
#print(es_pal([1,'pal']))
#--------------------------------------------------FIN----------------------------------------------------
def Pequal(alfa,beta):
    """
    pa determina si dos palabras son equibalente mente iguales
    pa(alfa,beta) --> boolean
    alfa: palabra
    beta: palabra
    """
    if alfa == [] and beta == []:
        return True
    elif alfa != [] and beta == []:
        return False
    elif  alfa == [] and beta != []:
        return False       
    elif alfa.pop() == beta.pop():
        return Pequal(alfa,beta)
    return False         
#-------------------------------------FIN---------------------------------------------------------
aux=[]
def p(*args):
    """
    esta definicion genera la concatenacion generalizada de una lista no determinada de palabras
    p(*args) ---> concatenacion generalizada
    *args: conjunto de palabras finitas (0 o mas palabras) 
    ejemplo: p([1,2,3],[x,y,z],[a,b,c]) ---> [1,2,3,x,y,z,a,b,c]
    """
    for x in args:
        if x != []:
            for s in x:
                aux.append(s)
    return aux    
#print(p([1,2,3],['x','y','z'],['a','b','c']))    
#_------------------------------------------FIN--------------------------------------------------------
def str_pal(str):
    """
    esta definicion convierte una palabra de type string a una aseptada de tipo lista
    str_pal(str) --> list
    str: string
    """
    for s in str:
        if s == 'ε':
           continue
        else:
           aux.append(s)
    return aux    
#print(str_pal('εhoεlaεmundo'))    
#-------------------------------------------------FIN-------------------------------------------------

def prefijo(a,w):
    """
    esta funcion determina si a es un prefijo de w
    prefijo(a,w) ---> boolean
    a: palabra
    w: palabra 
    """
    if a == []:
        return True
    elif len(a) <= len(w):
            p = w.pop()
            s = a.pop()
            for i in range(len(s)):
               if p[i] != s[i]:
                   return False
            return True                 
    else:
        return False    
#print(prefijo(['000'],['10011']))     
# ---------------------------------------FIn--------------------------------------------------------------

def sufijo(b,w):
    """
    esta funcion determina si a es un sufijo de w
    sufijo(a,w) ---> boolean
    a: palabra
    w: palabra
    """
    if b == []:
        return True
    elif len(b) <= len(w):
            p = w.pop()
            s = b.pop()
            p = p[::-1]
            s = s[::-1]
            for i in range(len(s)):
               if p[i] != s[i]:
                   return False
            return True                 
    else:
        return False   
#print(sufijo([""],["mundo"]))    
#---------------------------------FIN----------------------------------------------------
def sufijos(w):
    """
    esta funcion calcula toda la familia de sufijos de una apalabra w
    sufijos(w) ---> famila de sufijos
    w: palabra (warning: las palabras con espacio las con sidera tambien como simbolo si quiere espaciado recuerden usar ε) 
    """
    n =  ''
    pal = [()]
    if w == []:
        return w
    elif len(w) == 1:
        p = w.pop()
        p = p[::-1]
        for x in p:
             n = n + x
             pal.append(tuple(n[::-1]))          
        return pal
    else:
        return "violacion de contrato se esperaba una palabra y mandaste mas de una!"   
#print(sufijos(['alce']))
#----------------------------------------------------FIN--------------------------------------------
def prefijos(w):
    """
    esta funcion calcula toda la familia de sufijos de una apalabra w
    prefijos(w) ---> famila de sufijos
    w: palabra (warning: las palabras con espacio las con sidera tambien como simbolo si quiere espaciado recuerden usar ε) 
    """
    n =  ''
    pal = [()]
    if w == []:
        return w
    elif len(w) == 1:
        p = w.pop()
        for x in p:
             n = n + x
             pal.append(tuple(n))     
        return pal         
    else:
        return "violacion de contrato se esperaba una palabra y mandaste mas de una!"

#print(prefijos(['10011']))
#-----------------------------------------------------FIN---------------------------------------------
def gama(w):
    """
    esta funcion calcula gama de alfa,gama,beta
    gama(w) ---> familia de gama
    w: palabra
    """
    pal = []
    W = w.pop()
    W = list(W)
    for i in range(len(W)):
        pal.append(tuple(W[i]))
        if i < len(W)-1:
            aux = W[i] + W[i+1]
            pal.append(tuple(aux))
    return pal
#print(gama(['alce']))
#---------------------------------------------------FIn-----------------------------------------------------

def subpalabras(w):
    """
    esta funcion calcula toda la familia de sub palabras de w
    subpalabras(w) ---> familia de subpalabras
    w: palabra
    """
    z = w.copy()
    q = w.copy()
    pre = prefijos(z)
    ga = gama(q)
    su = sufijos(w)
    fam = pre + ga + su
    fam = set(fam)
    return list(fam)
#print(subpalabras(['alce']))    
#----------------------------------------------FIN------------------------------------------------------------------
def SgenL(L):
    GenL = []
    """
    esta funcion crea el alfabeto generador del lenguaje
    SgenL(L) --->  alfabeto
    L: lenguaje
    """
    for alf in L:
        for i in alf:
            if i not in GenL:
                GenL.append(i)
    return GenL
#print(SgenL([[0,1],[0,0,1],[0,1,1,1]]))
#------------------------------------------------Fin--------------------------------------------------------

def Lcard(L):
    """
    calcula la cardinalidad de un lenguaje
    Lcard(L) ---> number
    L: lenguaje
    """
    card = []

    if L == []:
        return 1
    else:
        for i in L:
            if i not in card:
                card.append(i)
        return len(card)
#print(Lcard([['h','h'],['j','j']]))
#-----------------------------------------------Fin-----------------------------------------

def pagoxarch(nomarch,cunit,longp):
    """
    calcula el pago por palabra de un archivo.
    pagoxarch(nomarch,cunit,longp) ---> number
    nomarch: String
    cunit: Number
    longp: Number
    """
    texto = []
    aux = ""
    cont = 0
    texto = txt_rel(nomarch) #definicion creada anteriormente
    for txt in texto:
        for i in txt:
                if i.isspace():
                    if len(aux) ==  longp:
                        cont += 1
                    aux="" 
                else:
                    aux += i
    return cont * cunit
#print(pagoxarch("palabras.txt",3,1))
#-------------------------------------------------Fin---------------------------------------------------
def lcon(L,M):
     """
     esta funcion concatena 2 lenguajes
     l(L,M) ---> lenguaje
     L: lenguaje
     M: lenguaje
     """
     aux = []
     aux2 = []
     for i in L:
         if i == []:
             i = ['']
         aux.append(i.pop(0))
     for j in M:
         if j == []:
            j = ['']
         aux2.append(j.pop(0))
     return list({(l+m)for l in aux for m in aux2})
#print(lcon([['x']],[['1'],['2']]))     
#-------------------------------------------------------Fin--------------------------------------------------------

def LconGen(*LLS):
    """
    esta funcion concatena 0 o mas lenguajes
    LconGen(args) ---> lenguaje
    args: lista no definida de 0 o mas lenguajes
    """
    LLS2 = []
    aux = []
    arl =  []
    for i in LLS:
        LLS2.append(i)
    aux = LLS2.pop(0) 
    if aux == [[]]:
        aux = LLS2.pop(0)       
    for n in LLS2:
      for j in range(len(n)):
          arl.append(n.pop()) 
    return lcon(aux,arl)
#print(LconGen([['01'],['00'],['10'],['11']],[['0'],['1']]))
#----------------------------------------------------------------FIN----------------------------------------------
auxKlen = []
def copylist(l):
    laux=[]
    for i in l:
        laux.append(i[:])
    return laux    

def lcongen(L,M):
     global auxKlen
     aux = []
     aux2 = []
     res = []
     l = copylist(L[:])
     m = copylist(M[:])
     for i in l:
         if i == []:
             i = ['']
         aux.append(i.pop(0))
     for j in m: 
         if j == []:
            j = ['']
         aux2.append(j.pop(0))
     for i in aux: 
         for n in aux2:
             res.append([i+n]) 
     auxKlen.append(res)                 
     return res 

# z = lcongen([['0'],['1']],[['0'],['1']])    
# print(z)      
# print(lcongen(z,[['0'],['1']]))
res 
ban = True
def potL(L,N):
    """
    esta funcion calcula la potencia de un lenguaje
    potL(L,N) ---> lenguaje
    N: number not negative
    """ 
    global res
    global ban
    aux = copylist(L[:])
    if N != 0:
       if ban == True:
            res = lcongen([[]],aux)
       else:   
            res = lcongen(res,aux)
       ban = False
       return potL(L,N-1)
    else:
       return res
#print(potL([['a'],['b']],3))    
#---------------------------------------------Fin-----------------------------------------------------
def nKleene(S,N):
    """
    debuelve la cerradura finita de kleeene hasta una potencia N de un alfabeto
    S:  alfabeto
    N: numero entero no negativo
    """
    global auxKlen
    auxKlen.append([])
    potL(S,N)
    return auxKlen
#nKleene([['1'],['0']],2)    
#-----------------------------------------------FIN---------------------------------------------------
def dat_tr(nomarch):
    """
    lee un archivo plano y la tranforma en una lista de transiciones
    dat_tr(nomarch) --> lista de tranciciones
    nomarch: String (ruta de archivo).
    """
    tex = [] 
    text = txt_rel(nomarch)
    for i in text:
        cont = 0
        init = ''
        texto = ''
        texto2 = ''
        for j in i:
            if j == '>' or  j == '-' or  j == '*':
                continue 
            else:
                if j == ' ':
                    cont += 1
                if cont == 1: 
                    if j != ' ': 
                        init += j
                if cont > 1 and cont < 4:
                    if j != '\n':
                        texto += j
                if cont >= 4:
                    if j != '\n':
                        texto2 += j
        tex.append(init + texto)
        tex.append(init + texto2)                       
               
    print(tex)            
    
#dat_tr('CF.txt')
#----------------------------------------------fin--------------------------------------------------------
def separar(s):
     """
     esta funcion sirve para separa los estados cuando uno va a dos al mismo tiempo
     separar(s) ---> lista con los estados separados
     s <--- lista con estados unidos
     """
     n = []
     x =  s.find(',')
     n.append(s[x-2:x])
     n.append(s[x+1:x+3])
     return n
def formatear(c):
    """
    esta funcion da un formato lejible para la clase afn
    formatear(c) ---> lista
    c <--- lista
    """
    formato = []
    aux2 = []
    for s in c:
        for x in s:
            if isinstance(x,list):
                for w in x:
                    for z in w:
                        formato.append(z)  
                    aux2.append(formato)    
                    formato = []      
            else:
                for q in x:
                    formato.append(q)  
                aux2.append(formato)    
                formato = []  
    return aux2   
class afn:
    """
    esta clase sirve para representacion de grafos y sus metodos
    se utiliza instanciando la clase de la siguente forma:
    AFN = afn() <--- se instacia como si llamaramos a una funcion
    AFN ---> este es un nuevo objeto que tiene acceso a todos los metodos y atributos de la clase afn
    """
    E = set()
    S = set()
    q0 = ""  
    T = set()
    A = set()
    dato = []
    d2 = []
    d = ""
    v = ""
    def __init__(self,e,s,q0,t,a):
        self.E = e
        self.s = s
        self.q0 = q0
        self.T = t
        self.A = a

    def EDOS(self,e):
        """
        metodo de estados añade al atributo E nuevos estados
        """
        self.E.add(e)
    def ALFA(self,s):
        """
        metodo de palabra añade al atributo S nuevos simbolos
        """
        self.S.add(s)
    def EINI(self,Q0):
        """
        metodo de estados inicial añade al atributo q0 el estado inicial
        """
        self.q0 += Q0
    def TRAN(self,t):
        """
        metodo de trancicion añade al atributo T todas las tranciciones
        """
        self.T.add(t)
    def ACEP(self,a):
        """
        metodo de estados aceptores añade al atributo A los estados aceptores
        """
        self.A.add(a)     
    def TR(self,e,s):
        """
        metodo de trancicion 
        """
        v = ""
        b = e +" "+s
        for alfa in self.T:
            if alfa.find(b) != -1:
                v = alfa                 
        v = v.replace(" "+b,"")
        v = v.replace(b,"")
        if v.find(',') != -1:
          return separar(v) 
        if v == " #":
              return e  
        return v
    def TRG(self,e,s):  
       """
       transicion generalizada
       """ 
       if s != []:
            self.d2 = [] 
            if isinstance(e,list):
                n = s.pop(0)
                for x in e:
                    if isinstance(x,list):
                       for l in x: 
                            l = " "+l
                            if l in e:
                                break
                            else:
                                self.d2.append(self.TR(l,n))
                    else:                        
                        self.d2.append(self.TR(x,n))         
                self.TRG(self.d2,s)   
            else:
                self.d = self.TR(e,s.pop(0))
                self.TRG(self.d,s)          
       if self.d2 == []:
           return self.d   
       else:          
           return self.d2
    def TRE(self,e,s):
        if e != []:
            for q in e:
                self.d2.append(self.TR(q,s))
        else:
            print('envia estados!')
        return self.d2 
    def TRAcep(self,e,s):
        res = self.TRE(e,s)
        for r in res:
            if isinstance(r,list):
                for r2 in r:
                    if r2 in self.A:
                        return True
            else:            
                if r in self.A:
                    return True
        return False                
    def nLeng(self,n):
        """
        metodo recibe como entrada opcional un numero entero positivo n y produce el conjunto de las palabras
        aceptadas de hasta longitud n inclusive.
        Afd.nLeng(n) ---> conjunto de palabras
        self <--- referencia a la clase afn
        n <--- numero entero positivo
        """
        asep = []
        alfa = list(self.S)
        alfa = [list(l) for l in alfa]
        conjunto = nKleene(alfa,n) 
        conjunto = formatear(conjunto)
        q2 = [] 
        for q in conjunto:
            q2 = q[:]
            v = self.TRG(self.q0,q)
            if isinstance(v,list):
                for i in v:
                    if isinstance(i,list):
                        for j in i:
                            if j == 'w4' or j == 'w5':
                                asep.append(q2)
                    else:
                        if i == 'w4' or i == 'w5':
                            asep.append(q2)            
                continue
            # else:
            #     for x in self.A:
            #         if v == " "+x:
            #             asep.append(q2)
            v =""                     
        print(asep)
    def acepta(self,w):
        """
        Este metodo recibe como entrada una palabra w y produce un valor booleano: #t si la palabra es aceptada y
        #f si la palabra no es aceptada.
        Afd.acepta(w) ---> bolean
        self <-- referencia a la clase afn
        w: palabra
        """
        
        res = self.TRG(self.q0,w)
        for r in res:
            if isinstance(r,list):
                for r2 in r:
                    r2 = r2.replace(" ","")  
                    if r2 in self.A:
                        return True
            else:  
                r = r.replace(" ","")       
                if r in self.A:
                    return True            
        return False 
    def Elog(self,w):
        elog = []
        i = 0
        while i < len(w):
            for s in w:
                if i == 0:
                    elog.append(self.q0)
                    elog.append(self.TR(self.q0,s))
                    i += 1
                else:    
                    elog.append(self.TR(elog[i],s))
                    i += 1
        return elog      
Afn = afn(set(),set(),"",set(),set())
#print(type(afd))
#-------------------------------------------------------------------------------------------------------------------
def leer_grafo(nomarch):
    """
    esta funcion recive el nomarch de un archivo .txt para tranformar en formato de grafo en la clase afd.
    leer_grafo(nomarch) --> llena con el formato de la clase afd
    nomarch: string
    nota al final de cada linea deja 1 espacio en blanco del archivo .txt
    """
    cont = 0
    asep = False
    init = False
    aux = ""
    aux2 = ""
    aux3 = 4
    val = 0
    tem = ""
    c = ""
    ed = ""
    if os.path.isfile(nomarch):
        archivo = open(nomarch, 'r')
        for linea in archivo:
           for l in linea:
               if l == " ":
                   cont += 1
               if cont == 0:
                   if l == ">":
                       init = True
                   if l == "*":   
                       asep = True
                       tem = ""  
               if cont == 1 and l != " ":
                   ed += l
                   if len(ed) == 2:
                        Afn.EDOS(ed)
                        ed = ""
                   if init and val < 2:
                       Afn.EINI(l)
                       val += 1      
                   if asep:
                       tem += l
                       if len(tem) == 2:
                            Afn.ACEP(tem) 
               if cont >= 2 and l != " " and l != "\n":
                   asep = False
                   if cont < 3:
                       Afn.ALFA(l)
                   if cont == 4 and cont < 5:
                       Afn.ALFA(l)                  
               if cont >= 1 and l != "\n":
                   if cont < 2:
                     aux += l
                     c += l
                   if cont < 4:
                       aux2 += l
                   else:  
                       if aux3 == cont :
                           if aux3 <= linea.count(" ") - 2:
                                aux3 += 2
                           else:
                               aux3 += 1      
                           if len(c) > 4:  
                             Afn.TRAN(c)
                             c = aux
                       c += l                        
           cont = 0                
           Afn.TRAN(aux2)
           c = ""
           aux = ""
           aux2 = ""  
           aux3 = 4          
        archivo.close()  
    else:
        print('el archivo no existe')    
leer_grafo('NX.txt')
#print(Afn.TRG("w1",['a','b','a','b'])) 
#print(Afn.TRAcep(["w1","w2","w5"],"b")) 
#print(Afn.acepta(["a","a","a","b"]))
#print(Afn.Elog(["0","0","1","0"]))
#Afn.nLeng(2)
#------------------------------------------fin-------------------------------------------------------------------
def EDEva(ed):
    cont = 0
    EDN = []
    c = ""
    for i in ed: 
        if i == " ":
            cont += 1
        if cont > 2 and i != " " and i != ",":
            if i != "#":
                c += i
                if len(c) == 2:
                    EDN.append(c)
                    c = ""
            else:         
                EDN.append(i)
    return EDN    

def buscar(t,q):
    """
    """
    tran = []
    c = ""
    for j in t:
        for i in Afn.S:
            w = j +" "+ i
            y = " "+i
            for tr in q:
                if tr.find(w) != -1:
                    tr = tr.replace(" "+w+" ","")
                    if ',' in tr:
                        for z in tr:
                            if z != ',':
                                c += z
                            elif  len(c) == 2:    
                                tran.append(c)
                                c = ""  
                        tran.append(c)
                        c = ""       
                    else:                 
                        tran.append(tr)                                                             
    return set(tran)

        
def Update_Trans(e,q):
    """
    esta fucion ingresa las tranciciones de los nuevos estados
    e <--- estados
    q <--- trancicion vieja
    """
    Ne = []
    b = []
    for i in e:
        if isinstance(i,tuple): 
            b.append(buscar(i,q))                 
    return Ne    
    


def ConverClass(Afn):
    """
    Esta funcion se encargar de convertir un afn %, en un nuevo afd %. La funcion debe recibir un objeto de la clase afn %, y devolver
    un objeto de la clase afn %.
    ConverClass(afn) ---> class object
    """
    ED = Afn.E
    SD = Afn.S
    AD = Afn.A
    TD = Afn.T
    q0D = Afn.q0
    listED = list(map(EDEva,TD))
    NED = list(map(lambda e: [e], ED))
    l = 0
    lon = len(listED)
    while l < lon:
        for j in ED:
            if listED[l] == [j]:
                del listED[l]
        l += 1
        lon = len(listED)        
    for i in listED: 
        ED.add(tuple(i))
    print(ED)       
    NTRD = Update_Trans(ED,TD)
    """
    no lo termine no le entendi cual era el problema ???
    """                      
ConverClass(Afn)
a = 5
b = 6
a += b
#print(a)
from functools import reduce
valores = [3,6,9,1]
#suma = reduce(lambda x, y = 0: (x > y) r = x else r = y , valores)
def mayor (*args):
   return reduce(lambda x , y: x > y, args)
mayor()   
print(mayor)
###############################################################################################################
