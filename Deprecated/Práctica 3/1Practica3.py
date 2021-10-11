class Problema(object):
    """Clase abstracta para un problema de espacio de estados. Los problemas
    concretos habría que definirlos como subclases de Problema, implementando
    acciones, aplica y eventualmente __init__, es_estado_final y
    coste_de_aplicar_accion. Una vez hecho esto, se han de crear instancias de
    dicha subclase, que serán la entrada a los distintos algoritmos de
    resolución mediante búsqueda."""  


    def __init__(self, estado_inicial, estado_final=None):
        """El constructor de la clase especifica el estado inicial y
        puede que un estado_final, si es que es único. Las subclases podrían
        añadir otros argumentos"""
        
        self.estado_inicial = estado_inicial
        self.estado_final = estado_final

    def acciones(self, estado):
        """Devuelve las acciones aplicables a un estado dado. Lo normal es
        que aquí se devuelva una lista, pero si hay muchas se podría devolver
        un iterador, ya que sería más eficiente."""
        abstract

    def aplica(self, estado, accion):
        """ Devuelve el estado resultante de aplicar accion a estado. Se
        supone que accion es aplicable a estado (es decir, debe ser una de las
        acciones de self.acciones(estado)."""
        abstract

    def es_estado_final(self, estado):
        """Devuelve True cuando estado es final. Por defecto, compara con el
        estado final, si éste se hubiera especificado al constructor. Si se da
        el caso de que no hubiera un único estado final, o se definiera
        mediante otro tipo de comprobación, habría que redefinir este método
        en la subclase.""" 
        return estado == self.estado_final

    def coste_de_aplicar_accion(self, estado, accion):
        """Devuelve el coste de aplicar accion a estado. Por defecto, este
        coste es 1. Reimplementar si el problema define otro coste """ 
        return 1
    
    
class Jarras(Problema):
    """Problema de las jarras:
    Representaremos los estados como tuplas (x,y) de dos números enteros,
    donde x es el número de litros de la jarra de 4 e y es el número de litros
    de la jarra de 3"""

    def __init__(self):
        super().__init__((0,0))

    def acciones(self,estado):
        jarra_de_4=estado[0]
        jarra_de_3=estado[1]
        accs=list()
        if jarra_de_4 > 0:
            accs.append("vaciar jarra de 4")
            if jarra_de_3 < 3:
                accs.append("trasvasar de jarra de 4 a jarra de 3")
        if jarra_de_4 < 4:
            accs.append("llenar jarra de 4")
            if jarra_de_3 > 0:
                accs.append("trasvasar de jarra de 3 a jarra de 4")
        if jarra_de_3 > 0:
            accs.append("vaciar jarra de 3")
        if jarra_de_3 < 3:
            accs.append("llenar jarra de 3")
        return accs

    def aplica(self,estado,accion):
        j4=estado[0]
        j3=estado[1]
        if accion=="llenar jarra de 4":
            return (4,j3)
        elif accion=="llenar jarra de 3":
            return (j4,3)
        elif accion=="vaciar jarra de 4":
            return (0,j3)
        elif accion=="vaciar jarra de 3":
            return (j4,0)
        elif accion=="trasvasar de jarra de 4 a jarra de 3":
            return (j4-3+j3,3) if j3+j4 >= 3 else (0,j3+j4)
        else: #  "trasvasar de jarra de 3 a jarra de 4"
            return (j3+j4,0) if j3+j4 <= 4 else (4,j3-4+j4)

    def es_estado_final(self,estado):
        return estado[0]==2
    
    
pj = Jarras()
pj.estado_inicial
# Resultado: (0, 0)
pj.acciones(pj.estado_inicial)
# Resultado: ['llenar jarra de 4', 'llenar jarra de 3']
pj.aplica(pj.estado_inicial,"llenar jarra de 4")
# Resultado: (4, 0)
pj.coste_de_aplicar_accion(pj.estado_inicial,"llenar jarra de 4")
# Resultado: 1
pj.es_estado_final(pj.estado_inicial)
# Resultado:False
pj.es_estado_final((2,3))


#################### EJERCICIO 1 #####################

class Ocho_Puzzle(Problema):
    def __init__(self,tablero_inicial):
        super().__init__(estado_inicial=tablero_inicial, estado_final=(1,2,3,8,0,4,7,6,5))

    def acciones(self,estado):
        pos_hueco=estado.index(0)
        accs=list()
        if pos_hueco not in [0,1,2]: 
            accs.append("Mover hueco arriba")
        if pos_hueco not in [6,7,8]: 
            accs.append("Mover hueco abajo")
        if pos_hueco not in [0,3,6]: 
            accs.append("Mover hueco izquierda")
        if pos_hueco not in [2,5,8]: 
            accs.append("Mover hueco derecha")
        return accs     

    def aplica(self,estado,accion):
        pos_hueco=estado.index(0)
        resl= list(estado)
        if accion=="Mover hueco arriba":
            nueva_pos = pos_hueco - 3
        elif accion=="Mover hueco abajo":
            nueva_pos = pos_hueco + 3
        elif accion=="Mover hueco izquierda":
            nueva_pos = pos_hueco - 1
        else:
            nueva_pos = pos_hueco + 1
        resl[pos_hueco],resl[nueva_pos] = resl[nueva_pos],resl[pos_hueco]
        return tuple(resl)
    
p8p_1 = Ocho_Puzzle((2, 8, 3, 1, 6, 4, 7, 0, 5))
p8p_1.estado_inicial
# Resultado: (2, 8, 3, 1, 6, 4, 7, 0, 5)
p8p_1.estado_final
# Resultado: (1, 2, 3, 8, 0, 4, 7, 6, 5)
p8p_1.acciones(p8p_1.estado_inicial)
# Resultado: ['Mover hueco arriba', 'Mover hueco izquierda', 'Mover hueco derecha']
p8p_1.aplica(p8p_1.estado_inicial,"Mover hueco arriba")
# Resultado: (2, 8, 3, 1, 0, 4, 7, 6, 5)
p8p_1.coste_de_aplicar_accion(p8p_1.estado_inicial,"Mover hueco arriba")
# Resultado: 1


######################### PARTE II  #####################
from AlgoritmosDeBusqueda import *


#################### EJERCICIO 2 #####################

búsqueda_en_anchura(Jarras()).solucion()
# Resultado:
# ['llenar jarra de 4', 'trasvasar de jarra de 4 a jarra de 3', 
#  'vaciar jarra de 3', 'trasvasar de jarra de 4 a jarra de 3', 
#  'llenar jarra de 4', 'trasvasar de jarra de 4 a jarra de 3']

búsqueda_en_profundidad(Jarras()).solucion()
# Resultado:
# ['llenar jarra de 3', 'trasvasar de jarra de 3 a jarra de 4', 
#  'llenar jarra de 3', 'trasvasar de jarra de 3 a jarra de 4', 
#  'vaciar jarra de 4', 'trasvasar de jarra de 3 a jarra de 4']

búsqueda_en_anchura(Ocho_Puzzle((2, 8, 3, 1, 6, 4, 7, 0, 5))).solucion()
# Resultado:
# ['Mover hueco arriba', 'Mover hueco arriba', 'Mover hueco izquierda', 
#  'Mover hueco abajo', 'Mover hueco derecha']

búsqueda_en_profundidad(Ocho_Puzzle((2, 8, 3, 1, 6, 4, 7, 0, 5))).solucion()
# Resultado:
# ['Mover hueco derecha', 'Mover hueco arriba', ... ] # ¡más de 3000 acciones!


#################### EJERCICIO 3 #####################

def h1_ocho_puzzle(estado):
    cont=0
    for x,y in zip(estado,(1,2,3,8,0,4,7,6,5)):
        if x !=0 and x != y: cont += 1
    return cont

def h2_ocho_puzzle(estado):
    posiciones_final=(4,0,1,2,5,8,7,6,3)
    suma=0
    
    for i in range(9):
        estadoi=estado[i]
        if estadoi != 0:
            j=posiciones_final[estadoi]
            
            i_x,i_y=divmod(i,3)
            j_x,j_y=divmod(j,3)
            suma += abs(i_x-j_x)+abs(i_y-j_y)
    return suma


h1_ocho_puzzle((2, 8, 3, 1, 6, 4, 7, 0, 5))
# Resulatado: 4
h2_ocho_puzzle((2, 8, 3, 1, 6, 4, 7, 0, 5))
# Resultado: 5
h1_ocho_puzzle((5,2,3,0,4,8,7,6,1))
# Resultado: 4
h2_ocho_puzzle((5,2,3,0,4,8,7,6,1))
# Resultado: 11


#################### EJERCICIO 4 #####################

# Estado inicial

#              +---+---+---+
#              | 2 | 8 | 3 |
#              +---+---+---+
#              | 1 | 6 | 4 |
#              +---+---+---+
#              | 7 | H | 5 |
#              +---+---+---+

búsqueda_óptima(Ocho_Puzzle((2, 8, 3, 1, 6, 4, 7, 0, 5))).solucion()
# Resultado:
# ['Mover hueco arriba', 'Mover hueco arriba', 'Mover hueco izquierda', 
#  'Mover hueco abajo', 'Mover hueco derecha']

búsqueda_primero_el_mejor(Ocho_Puzzle((2, 8, 3, 1, 6, 4, 7, 0, 5)),h1_ocho_puzzle).solucion()
# Resultado:
# ['Mover hueco arriba', 'Mover hueco izquierda', 'Mover hueco arriba', 
#  'Mover hueco derecha', 'Mover hueco abajo', 'Mover hueco izquierda', 
#  'Mover hueco arriba', 'Mover hueco derecha', 'Mover hueco abajo']

búsqueda_primero_el_mejor(Ocho_Puzzle((2, 8, 3, 1, 6, 4, 7, 0, 5)),h2_ocho_puzzle).solucion()
# Resultado:
# ['Mover hueco arriba', 'Mover hueco arriba', 'Mover hueco izquierda', 
#  'Mover hueco abajo', 'Mover hueco derecha']

búsqueda_a_estrella(Ocho_Puzzle((2, 8, 3, 1, 6, 4, 7, 0, 5)),h1_ocho_puzzle).solucion()
# Resultado:
# ['Mover hueco arriba', 'Mover hueco arriba', 'Mover hueco izquierda', 
#  'Mover hueco abajo', 'Mover hueco derecha']

búsqueda_a_estrella(Ocho_Puzzle((2, 8, 3, 1, 6, 4, 7, 0, 5)),h2_ocho_puzzle).solucion()
# Resultado:
# ['Mover hueco arriba', 'Mover hueco arriba', 'Mover hueco izquierda', 
#  'Mover hueco abajo', 'Mover hueco derecha']


######################### PARTE III  #####################

class Problema_con_Analizados(Problema):

    """Es un problema que se comporta exactamente igual que el que recibe al
       inicializarse, y además incorpora un atributos nuevos para almacenar el
       número de nodos analizados durante la búsqueda. De esta manera, no
       tenemos que modificar el código del algorimo de búsqueda.""" 
         
    def __init__(self, problema):
        self.estado_inicial = problema.estado_inicial
        self.problema = problema
        self.analizados  = 0

    def acciones(self, estado):
        return self.problema.acciones(estado)

    def aplica(self, estado, accion):
        return self.problema.aplica(estado, accion)

    def es_estado_final(self, estado):
        self.analizados += 1
        return self.problema.es_estado_final(estado)

    def coste_de_aplicar_accion(self, estado, accion):
        return self.problema.coste_de_aplicar_accion(estado,accion)



def resuelve_ocho_puzzle(estado_inicial, algoritmo, h=None):
    """Función para aplicar un algoritmo de búsqueda dado al problema del ocho
       puzzle, con un estado inicial dado y (cuando el algoritmo lo necesite)
       una heurística dada.
       Ejemplo de uso:

       >>> resuelve_ocho_puzzle((2, 8, 3, 1, 6, 4, 7, 0, 5),búsqueda_a_estrella,h2_ocho_puzzle)
       Solución: ['Mover hueco arriba', 'Mover hueco arriba', 'Mover hueco izquierda', 
                  'Mover hueco abajo', 'Mover hueco derecha']
       Algoritmo: búsqueda_a_estrella
       Heurística: h2_ocho_puzzle
       Longitud de la solución: 5. Nodos analizados: 7
       """

    p8p=Problema_con_Analizados(Ocho_Puzzle(estado_inicial))
    sol= (algoritmo(p8p,h).solucion() if h else algoritmo(p8p).solucion()) 
    print("Solución: {0}".format(sol))
    print("Algoritmo: {0}".format(algoritmo.__name__))
    if h: 
        print("Heurística: {0}".format(h.__name__))
    else:
        pass
    print("Longitud de la solución: {0}. Nodos analizados: {1}".format(len(sol),p8p.analizados))
    
    
#################### EJERCICIO 5 #####################    

#           E1              E2              E3              E4
#           
#     +---+---+---+   +---+---+---+   +---+---+---+   +---+---+---+    
#     | 2 | 8 | 3 |   | 4 | 8 | 1 |   | 2 | 1 | 6 |   | 5 | 2 | 3 |
#     +---+---+---+   +---+---+---+   +---+---+---+   +---+---+---+
#     | 1 | 6 | 4 |   | 3 | H | 2 |   | 4 | H | 8 |   | H | 4 | 8 |
#     +---+---+---+   +---+---+---+   +---+---+---+   +---+---+---+
#     | 7 | H | 5 |   | 7 | 6 | 5 |   | 7 | 5 | 3 |   | 7 | 6 | 1 |
#     +---+---+---+   +---+---+---+   +---+---+---+   +---+---+---+ 

resuelve_ocho_puzzle((2,8,3,1,6,4,7,0,5),búsqueda_en_anchura)

resuelve_ocho_puzzle((2,8,3,1,6,4,7,0,5),búsqueda_en_profundidad)

# -----------------------------------------------------------------------------------------
#                                       E1           E2           E3          E4
                                
# Anchura                             L=            L=           L=          L=  
#                                     NA=           NA=          NA=         NA= 
                                                                              
# Profundidad                         L=            L=           L=          L=  
#                                     NA=           NA=          NA=         NA= 
                                                                              
# Óptima                              L=            L=           L=          L=  
#                                     NA=           NA=          NA=         NA= 
                                                                              
# Primero el mejor (h1)               L=            L=           L=          L=
#                                     NA=           NA=          NA=         NA=
                                                                              
# Primero el mejor (h2)               L=            L=           L=          L= 
#                                     NA=           NA=          NA=         NA=
                                                                              
# A* (h1)                             L=            L=           L=          L= 
#                                     NA=           NA=          NA=         NA=
                                                                              
# A* (h2)                             L=            L=           L=          L= 
#                                     NA=           NA=          NA=         NA=

# -----------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------
#                                       E1           E2           E3          E4
                                
# Anchura                             L= 5          L= 12        L= -        L= -
#                                     NA=35         NA=2032      NA=-        NA=-
                                                                              
# Profundidad                         L= 3437       L= -         L= -        L= -
#                                     NA=3528       NA=-         NA=-        NA=-
                                                                              
# Óptima                              L= 5          L= 12        L= -        L= -
#                                     NA=53         NA=2049      NA=-        NA=-
                                                                              
# Primero el mejor (h1)               L= 9          L= 20        L= 134      L= 105
#                                     NA=11         NA=24        NA=575      NA=1002
                                                                              
# Primero el mejor (h2)               L= 5          L= 12        L= 28       L= 37
#                                     NA=7          NA=15        NA=196      NA=177
                                                                              
# A* (h1)                             L= 5          L= 12        L= 18       L= 25
#                                     NA=8          NA=91        NA=1290     NA=23209
                                                                              
# A* (h2)                             L= 5          L= 12        L= 18       L= 25
#                                     NA=7          NA=15        NA=138      NA=1273


#################### EJERCICIO 6 #####################

def h3_ocho_puzzle(estado):

    suc_ocho_puzzle ={0: 1, 1: 2, 2: 5, 3: 0, 4: 4, 5: 8, 6: 3, 7: 6, 8: 7}  

    def secuencialidad_aux(estado,i):
        
        val=estado[i]
        if val == 0:
            return 0
        elif i == 4:
            return 1
        else:
            i_sig=suc_ocho_puzzle[i]
            val_sig = (val+1 if val<8 else 1)
            return 0 if val_sig == estado[i_sig] else 2 

    def secuencialidad(estado):
        res= 0 
        for i in range(8): 
            res+=secuencialidad_aux(estado,i)
        return res    

    return h2_ocho_puzzle(estado) + 3*secuencialidad(estado)