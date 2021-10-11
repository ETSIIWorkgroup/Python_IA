#################################### PRÁCTICA 4 #############################################################################
#
# Procesos de decisión de Markov
# 
##############################################################################################################################

import random

class MDP(object):

    """La clase genérica MDP tiene como métodos la función de recompensa R,
    la función A que da la lista de acciones aplicables a un estado, y la
    función T que implementa el modelo de transición. Para cada estado y
    acción aplicable al estado, la función T devuelve una lista de pares
    (ei,pi) que describe los posibles estados ei que se pueden obtener al
    plical la acción al estado, junto con la probabilidad pi de que esto
    ocurra. El constructor de la clase recibe la lista de estados posibles y
    el factor de descuento.

    En esta clase genérica, las funciones R, A y T aparecen sin definir. Un
    MDP concreto va a ser un objeto de una subclase de esta clase MDP, en la
    que se definirán de manera concreta estas tres funciones"""  

    def __init__(self,estados,descuento):

        self.estados=estados
        self.descuento=descuento

    def R(self,estado):
        pass

    def A(self,estado):
        pass
        
    def T(self,estado,accion):
        pass
    
    
########### EJERCICIO 1 ################

class Rica_y_Conocida(MDP):
    
    def __init__(self,descuento=0.9):
        # RC: rica y conocida, RD: rica y desconocida, 
        # PC: pobre y conocida, PD: pobre y desconocida 
        self.Rdict={"RC":10,"RD":10,"PC":0,"PD":0}
        self.Tdict={("RC","No publicidad"):[("RC",0.5),("RD",0.5)],
                    ("RC","Gastar en publicidad"):[("PC",1)],
                    ("RD","No publicidad"):[("RD",0.5),("PD",0.5)],
                    ("RD","Gastar en publicidad"):[("PD",0.5),("PC",0.5)],
                    ("PC","No publicidad"):[("PD",0.5),("RC",0.5)],        
                    ("PC","Gastar en publicidad"):[("PC",1)],
                    ("PD","No publicidad"):[("PD",1)],
                    ("PD","Gastar en publicidad"):[("PD",0.5),("PC",0.5)]}
        super().__init__(["RC","RD","PC","PD"],descuento)
        
    def R(self,estado):
        return self.Rdict[estado]
        
    def A(self,estado):
        return ["No publicidad","Gastar en publicidad"]
        
    def T(self,estado,accion):
        return self.Tdict[(estado,accion)]    
    
    
########### EJERCICIO 2 ################    

# distr es un lista de pares (vi,pi) con los diferentes valores de la v.a. y
# sus probabilidades. 
def muestreo(distr):
    r=random.random()
    acum=0
    for v,p in distr:
        acum+=p
        if acum>r:
            return v

# Devuelve un valor y su probabilidad        
def muestreo_2(distr):
    r=random.random()
    acum=0
    for v,p in distr:
        acum+=p
        if acum>r:
            return v,p
        
        
def genera_secuencia_estados(mdp,pi,e,n):
    actual=e
    seq=[actual]
    for _ in range(n-1):
        actual=muestreo(mdp.T(actual,pi[actual]))
        seq.append(actual)
    return seq

# Devuelve la secuencia de estados y su probabilidad
def genera_secuencia_estados_2(mdp,pi,e,n):
    actual=e
    ac_prob = 1
    seq=[actual]
    for _ in range(n-1):
        actual,prob = muestreo(mdp.T(actual,pi[actual]))
        seq.append(actual)
        ac_prob *= prob
    return seq,ac_prob

# Definimos una instancia de la subclase 
mdp_ryc=Rica_y_Conocida()

pi_ryc_ahorra={"RC":"No publicidad","RD":"No publicidad",
                    "PC":"No publicidad","PD":"No publicidad"}
genera_secuencia_estados(mdp_ryc,pi_ryc_ahorra,"PC",10)

# Posible resultado:
# ['PC', 'PD', 'PD', 'PD', 'PD', 'PD', 'PD', 'PD', 'PD', 'PD']

pi_ryc_2={"RC":"No publicidad","RD":"Gastar en publicidad",
               "PC":"No publicidad","PD":"Gastar en publicidad"}
genera_secuencia_estados(mdp_ryc,pi_ryc_2,"RD",8)

# Posible resultado:
# ['RD', 'PC', 'RC', 'RC', 'RC', 'RC', 'RD', 'PC']


########### EJERCICIO 3 ################  

def valora_secuencia(seq,mdp):
    return sum(mdp.R(e)*(mdp.descuento**i) for i,e in enumerate(seq))
   

# def valora_secuencia(seq,mdp):
#     suma=0
#     i=0
#     for e in seq:
#         suma+=mdp.R(e)*(mdp.descuento**i)
#         i+=1
#     return suma

valora_secuencia(['PC', 'RC', 'RC', 'RC', 'RC', 'RC', 
                       'RD', 'RD', 'RD', 'PD', 'PD', 'PD', 
                       'PD', 'PD', 'PD', 'PD', 'PD', 'PD', 
                       'PD', 'PD'],mdp_ryc)

# Resultado:
# 51.2579511

valora_secuencia(['RD', 'PC', 'PD', 'PC', 'RC', 'RC', 
                        'RD', 'PD', 'PD', 'PC', 'RC', 'RC', 
                        'RC', 'RC', 'RC', 'RC'],mdp_ryc)

# Resultado:
# 44.11795212148159


########### EJERCICIO 4 ################  

def estima_valor(e,pi,mdp,m,n):
    return (sum(valora_secuencia(genera_secuencia_estados(mdp,pi,e,m),mdp) 
                for _ in range(n)))/n

# Usando genera_secuencia_estados_2
def estima_valor_2(e,pi,mdp,m,n):
    suma = 0
    for _ in range(n):
        seq, prob = genera_secuencia_estdo_2(mdp,pi,e,m)
        val = valora_secuencia(seq)
        suma += val * prob
    return suma

estima_valor("PC",pi_ryc_ahorra,mdp_ryc,50,500)

# Respuesta posible:
# 14.531471247172597

estima_valor("PC",pi_ryc_2,mdp_ryc,50,500)

# Respuesta posible:
# 35.92126959549151

estima_valor("RC",pi_ryc_ahorra,mdp_ryc,60,700)

# Respuesta posible:
# 32.807558694112984

estima_valor("RC",pi_ryc_2,mdp_ryc,60,700)

# Respuesta posible:
# 50.09728516585913


########### EJERCICIO 5 ################ 

pi_ryc_gastar={"RC":"Gastar en publicidad","RD":"Gastar en publicidad",
                  "PC":"Gastar en publicidad","PD":"Gastar en publicidad"}
pi_ryc_ahorra={"RC":"No publicidad","RD":"No publicidad",
                    "PC":"No publicidad","PD":"No publicidad"}

estima_valor("RC",pi_ryc_gastar,mdp_ryc,60,1000)

# Respuesta: 10.0

estima_valor("RC",pi_ryc_ahorra,mdp_ryc,60,1000)

# Respuesta: 33.354461818277635

estima_valor("RD",pi_ryc_gastar,mdp_ryc,60,1000)

# Respuesta: 10.0

estima_valor("RD",pi_ryc_ahorra,mdp_ryc,60,1000)

# Respuesta:18.17532275274187

estima_valor("PC",pi_ryc_gastar,mdp_ryc,60,1000)

# Respuesta: 0.0

estima_valor("PC",pi_ryc_ahorra,mdp_ryc,60,1000)

# Respuesta: estima_valor("PC",pi_ryc_ahorra,mdp_ryc,60,1000)

estima_valor("PD",pi_ryc_gastar,mdp_ryc,60,1000)

# Respuesta: 0.0


########### EJERCICIO 6 ################ 

def valoración_respecto_política(pi,mdp, k):
    """Calcula una aproximación a la valoración de los estados respecto de la
    política pi, aplicando el método iterativo"""
    R, T, gamma = mdp.R, mdp.T, mdp.descuento
    V = {e:0 for e in mdp.estados}
    for _ in range(k):
        V1 = V.copy()
        for s in mdp.estados:
            V[s] = R(s) + gamma *(sum([p * V1[s1] for (s1,p) in T(s, pi[s])]))
    return V


valoración_respecto_política(pi_ryc_gastar,mdp_ryc, 100)

# Resultado:
# {'RC': 10.0, 'RD': 10.0, 'PC': 0.0, 'PD': 0.0}

valoración_respecto_política(pi_ryc_ahorra,mdp_ryc, 100)

# Resultado:
# {'RC': 33.05785123966942,
#  'RD': 18.18181818181818,
#  'PC': 14.876033057851238,
#  'PD': 0.0}


########### EJERCICIO 7 ################

def argmax(seq,f):
    max=float("-inf")
    amax=None
    for x in seq:
        fx=f(x)
        if fx>max:
            max=fx
            amax=x
    return amax

def valoración_esperada(acc,estado,V,mdp):
    """ Encuentra la valoración esperada de una acción respecto de una función
    de valoración V"""

    return sum((p * V[e] for (e,p) in mdp.T(estado, acc)))


def iteración_de_políticas(mdp,k):
    "Algoritmo de iteración de políticas"
    V = {e:0 for e in mdp.estados}
    pi = {e:random.choice(mdp.A(e)) for e in mdp.estados}
    while True:
        V = valoración_respecto_política(pi,mdp, k)
        actualizado = False
        for e in mdp.estados:
            acc = argmax(mdp.A(e), lambda a:valoración_esperada(a, e,V, mdp))
            if (acc != pi[e] and 
                valoración_esperada(acc, e,V, mdp) > valoración_esperada(pi[e], e,V, mdp)): # Por si hay empate
                pi[e] = acc
                actualizado = True
        if not actualizado:
            return pi,V

iteración_de_políticas(mdp_ryc,100)

# Respuesta
# ({'RC': 'No publicidad',
#   'RD': 'No publicidad',
#   'PC': 'No publicidad',
#   'PD': 'Gastar en publicidad'},
#  {'RC': 54.20053629623792,
#   'RD': 44.02311379672535,
#   'PC': 38.602953921506,
#   'PD': 31.584041852876634})