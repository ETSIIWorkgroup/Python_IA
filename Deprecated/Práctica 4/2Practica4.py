import random

class MDP(object):

    """La clase genérica MDP tiene como métodos la función de recompensa R,
    la función A que da la lista de acciones aplicables a un estado, y la
    función T que implementa el modelo de transición. Para cada estado y
    acción aplicable al estado, la función T devuelve una lista de pares
    (ei,pi) que describe los posibles estados ei que se pueden obtener al
    aplicar la acción al estado, junto con la probabilidad pi de que esto
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
    
    
class Cuadrícula(MDP):
    """Supondremos que cuadrícula viene dada por una lista de listas, en la
    que si hay un número es la recompensa de esa casilla, si hay otra cosa la
    recompesa es la que se indica por defecto y si hay None es una casilla
    bloqueada. Supondremos que está bien construida"""

    def __init__(self,cuadrícula,recompensa_por_defecto=-0.04,descuento=0.9,ruido=0.2):

        estados=[]
        terminales=[]
        recompensa={}
        nfilas=len(cuadrícula)
        ncolumnas=len(cuadrícula[0])
        for i in range(nfilas):
            for j in range(ncolumnas):
                contenido=cuadrícula[i][j]
                if contenido != "*":
                    estados.append((i,j))
                    if isinstance(contenido,(int,float)):
                        recompensa[(i,j)]=contenido
                        terminales.append((i,j))
                    else:
                        recompensa[(i,j)]=recompensa_por_defecto
                        if contenido=='S':
                            estado_inicial=(i,j)
                    
        super().__init__(estados,descuento)
        self.estados_terminales=terminales
        self.nfilas=nfilas
        self.ncolumnas=ncolumnas
        self.recompensa=recompensa
        self.ruido=ruido
        self.desplazamientos={"arriba":[(-1,0),(0,-1),(0,1)],
                                         "abajo":[(1,0),(0,-1),(0,1)],
                                         "izquierda":[(0,-1),(-1,0),(1,0)],
                                         "derecha":[(0,1),(-1,0),(1,0)]}


    def R(self,estado):
        return self.recompensa[estado]

    def A(self,estado):
        if estado in self.estados_terminales:
            return ["exit"]
        else:
            return ["arriba","abajo","izquierda","derecha"]

    def T(self,estado,acción):

        def desplaza(estado,despl):
            x,y=estado
            i,j=despl
            nx,ny=x+i,y+j
            if (nx,ny) in self.estados:
                return nx,ny
            else:
                return x,y

        if acción=="exit":
            return([(estado,0)])
        else:
            despl=self.desplazamientos[acción]
            pok=1-self.ruido
            pnook=self.ruido/2
            return [(desplaza(estado,despl[0]),pok),
                      (desplaza(estado,despl[1]),pnook),
                      (desplaza(estado,despl[2]),pnook)]
            

cuadrícula_1 = [[' ',' ',' ',+1],
                [' ','*',' ',-1],
                [' ',' ',' ',' ']]

            
            
            
cuad1_MDP=Cuadrícula(cuadrícula_1,descuento=0.8)


cuad1_MDP.estados
cuad1_MDP.estados_terminales
cuad1_MDP.R((0,3))
cuad1_MDP.R((1,3))
cuad1_MDP.R((2,1))
cuad1_MDP.A((0,3))
cuad1_MDP.A((1,3))
cuad1_MDP.A((0,2))
cuad1_MDP.T((2,2),"izquierda")
cuad1_MDP.T((2,1),"izquierda")


pi1={(0,0):"derecha",
     (0,1):"derecha",
     (0,2):"derecha",
     (0,3):"exit",
     (1,0):"arriba",
     (1,2):"arriba",
     (1,3):"exit",
     (2,0):"arriba",
     (2,1):"izquierda",
     (2,2):"izquierda",
     (2,3):"izquierda"}  


# distr es un lista de pares (vi,pi) con los diferentes valores de la v.a. y
# sus probabilidades. 
def muestreo(distr):
    r=random.random()
    acum=0
    for v,p in distr:
        acum+=p
        if acum>r:
            return v
            
def genera_secuencia_estados(mdp,pi,e,n):
    actual=e
    seq=[actual]
    for _ in range(n-1):
        if actual in mdp.estados_terminales:
            break
        actual=muestreo(mdp.T(actual,pi[actual]))
        seq.append(actual)
    return seq

genera_secuencia_estados(cuad1_MDP,pi1,(2,2),15)
genera_secuencia_estados(cuad1_MDP,pi1,(2,2),15)
genera_secuencia_estados(cuad1_MDP,pi1,(2,2),15)

def valora_secuencia(seq,mdp):
    return sum(mdp.R(e)*(mdp.descuento**i) for i,e in enumerate(seq))  

valora_secuencia([(2, 2), (2, 1), (2, 0), (1, 0), (0, 0), (0, 0), (0, 1), (0, 2), (0, 3)],cuad1_MDP)

# Resultado:
# 0.001326592000000043

valora_secuencia([(2, 2), (1, 2), (0, 2), (0, 3)],cuad1_MDP)
# Resultado:
# 0.4144000000000001

valora_secuencia([(2, 2),(2, 2),(2, 2),(2, 1),(2, 1),(2, 1),(2, 0),
                 (1, 0),(1, 0),(0, 0),(0, 1),(0, 2),(0, 3)],cuad1_MDP)

# Resultado:
# -0.11753662791680003

# Solución:

def estima_valor(e,pi,mdp,m,n):
    return (sum(valora_secuencia(genera_secuencia_estados(mdp,pi,e,m),mdp) 
                for _ in range(n)))/n

cuad2_MDP=Cuadrícula(cuadrícula_1,descuento=1)
estima_valor((0,0),pi1,cuad2_MDP,15,100000)
estima_valor((2,2),pi1,cuad2_MDP,15,100000)
estima_valor((0,2),pi1,cuad2_MDP,15,100000)
estima_valor((2,3),pi1,cuad2_MDP,15,100000)
estima_valor((1,2),pi1,cuad2_MDP,15,100000)