#################################### PRÁCTICA 1 #############################################################################
#
# En esta práctica se verá la implementación en Python del algoritmo de enfriamiento simulado y su uso para 
# intentar resolver distintos casos concretos del problema del viajante.
# 
# La práctica se estructura en tres partes:
#   En la primera parte, vamos a implementar la representación del problema del viajante para problemas de búsqueda local.
#   En la segunda implementaremos el algoritmo de enfriamiento simulado.
#   En la tercera parte, lo aplicaremos para resolver distintos problemas del viajante.
##############################################################################################################################


# Librerias
import random
import math

# Clase Problema de busqueda local
class Problema_Busqueda_Local(object):
    """Clase abstracta para un problema de búsqueda local. Los problemas
    concretos habría que definirlos como subclases de esta clase,
    implementando genera_estado_inicial, genera_sucesor y valoración. Como
    atributo de dato, tendremos "mejor", que va a almacenar la función "menor
    que", o "mayor que" dependiendo de que se trate, respectivamente, de
    minimizar o maximizar."""     


    def __init__(self,mejor=lambda x,y: x < y ):
        self.mejor=mejor

    def genera_estado_inicial(self):
        """Genera, posiblemente con cierta componente aleatoria y heurística,
           un estado para empezar la búsqueda ."""
        abstract
        
    def genera_sucesor(self, estado):
        """ Devuelve un estado "sucesor" del que recibe como
            entrada. Usualmente, esta función tendrá cierta componente
            aleatoria y heurística."""
        abstract

    def valoracion(self, estado):
        """Devuelve la valoración de un estado. Es el valor a optimizar."""  
        abstract

########### EJERCICIO 1 ################

# Clase ViajanteBusquedaLocal
class Viajante_BL(Problema_Busqueda_Local):
    
    def __init__(self, ciudades_coords):
        super().__init__()
        self.ciudades_coords = ciudades_coords
        self.num_ciudades = len(ciudades_coords)
        
    def genera_estado_inicial(self):
        ciudades = list(self.ciudades_coords.keys())
        random.shuffle(ciudades)
        
        return ciudades
    
    def genera_sucesor(self, estado):
        fst = random.randint(0, self.num_ciudades - 1)
        snd = (fst + random.randint(1, self.num_ciudades - 3)) % self.num_ciudades
        
        if fst < snd:
            sucesor = estado[:]
            sucesor[fst:snd+1] = sucesor[fst:snd+1][::-1]
        else:
            sucesor = estado[fst:][::-1] + estado[snd+1:fst] + estado[:snd+1][::-1]
        
        return sucesor
    
    def valoracion(self, estado):
        num_ciudades = len(estado)
        
        return sum([distancia_euc2D(estado[i], estado[(i+1) % num_ciudades], self.ciudades_coords) for i in range(num_ciudades)])

    
########### EJERCICIO 2 ################

def distancia_euc2D(c1,c2,coords):
    """ Función que recibe dos ciudades y devuelve la distancia entre ellas,
    calculada mediante distancia euclidea en el plano. El tercer argumento de
    la función contiene las coordenadas de todas las ciudades del problema (en
    foma de lista o de diccionario)""" 
    coord_c1= coords[c1]
    coord_c2= coords[c2]
    return math.hypot(coord_c1[0]-coord_c2[0],coord_c1[1]-coord_c2[1])

andalucia={"almeria": (409.5, 93),
           "cadiz":(63, 57),
           "cordoba": (198, 207),
           "granada": (309, 127.5),
           "huelva":  (3, 139.5),
           "jaen":    (295.5, 192),
           "malaga":  (232.5,  75),
           "sevilla": ( 90, 153)}

viajante_andalucia = Viajante_BL(andalucia)

circuito=viajante_andalucia.genera_estado_inicial() 

circuito

viajante_andalucia.genera_sucesor(circuito)

circuito_suc = viajante_andalucia.genera_sucesor(circuito)
circuito_suc


########### EJERCICIO 3 ################

def sorteo(p):
    if random.random() < p:
        return True
    else: 
        return False

def experimento (p,n):
    cont=0
    for _ in range(n):
        if sorteo(p):
            cont += 1
    return cont/n 

# Prueba
experimento(0.3,100000)


########### EJERCICIO 4 ################

def aceptar_e_s(valor_candidata, valor_actual, T, mejor):
    if mejor(valor_candidata, valor_actual):
        return True
    else:
        exponente = -(valor_candidata - valor_actual) / T
        return sorteo(math.exp(exponente))
    
# Ejemplo de uso
aceptar_e_s(12,11.5,10,lambda x,y: x < y)

# Posible respuesta;
# True

########### EJERCICIO 5 ################

def enfriamiento_simulado(problema, t_inicial, factor_descenso, n_enfriamientos, n_iteraciones):
    
    #Recibe como entrada:
    # Un problema de busqueda local
    # Una temperatura inicial
    # Un factor de descenso
    # Un nº total de enfriamientos
    # Un nº total de iteraciones para cada T
    
    actual = problema.genera_estado_inicial()
    valor_actual = problema.valoracion(actual)
    mejor = actual
    valor_mejor = valor_actual
    T = t_inicial
    
    for _ in range(n_enfriamientos):
        for _ in range(n_iteraciones):
            candidata = problema.genera_sucesor(actual)
            valor_candidata = problema.valoracion(candidata)
            
            if aceptar_e_s(valor_candidata, valor_actual, T, problema.mejor):
                actual = candidata
                valor_actual = valor_candidata
                
                if problema.mejor(valor_actual, valor_mejor):
                    mejor = actual
                    valor_mejor = valor_actual
        T *= factor_descenso
    return (mejor, valor_mejor)
                    

########### EJERCICIO 6 ################

enfriamiento_simulado(viajente_andalucia, 10, 0.95, 20, 20)

# Posible respuesta: 
# (['malaga', 'cadiz', 'huelva', 'sevilla', 'cordoba', 'jaen', 'almeria',
#   'granada'], 
#   929.9255755927754)


########### EJERCICIO 7 ################

def cuadrado_puntos_bl(n):
    ciudades_coords = {}
    id_ciudad = 0
    
    for i in range(n+1):
        ciudades_coords[id_ciudad] = (0, i)
        ciudades_coords[id_ciudad + 1] = (n, i)
        id_ciudad += 2
        
        if i not in (0, n):
            ciudades_coords[id_ciudad] = (i, 0)
            ciudades_coords[id_ciudad + 1] = (i, n)
            id_ciudad += 2
            
    return Viajante_BL(ciudades_coords)

enfriamiento_simulado(cuadrado_puntos_bl(3), 5, 0.95, 100, 100)

# Posible respuesta:
# ([(2, 0), (3, 0), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (0, 3), 
#   (0, 2), (0, 1), (0, 0), (1, 0)], 
#  12.0)

enfriamiento_simulado(cuadrado_puntos_bl(15), 35, 0.95, 100, 100)[1]

# Posible respuesta
# 74.0


########### EJERCICIO 8 ################

# Problema Berlin 52:
# 52 lugares de Berlin (Groetschel)
# La ruta óptima está valorada en 7542
# La siguiente variable contiene las coordinadas de los lugares. La distancia
# entre ciudades es la euclídea en dos dimensiones.

berlin52=[(565.0, 575.0),
        (25.0, 185.0),
        (345.0, 750.0),
        (945.0, 685.0),
        (845.0, 655.0),
        (880.0, 660.0),
        (25.0, 230.0),
        (525.0, 1000.0),
        (580.0, 1175.0),
        (650.0, 1130.0),
        (1605.0, 620.0 ),
        (1220.0, 580.0),
        (1465.0, 200.0),
        (1530.0, 5.0),
        (845.0, 680.0),
        (725.0, 370.0),
        (145.0, 665.0),
        (415.0, 635.0),
        (510.0, 875.0  ),
        (560.0, 365.0),
        (300.0, 465.0),
        (520.0, 585.0),
        (480.0, 415.0),
        (835.0, 625.0),
        (975.0, 580.0),
        (1215.0, 245.0),
        (1320.0, 315.0),
        (1250.0, 400.0),
        (660.0, 180.0),
        (410.0, 250.0),
        (420.0, 555.0),
        (575.0, 665.0),
        (1150.0, 1160.0),
        (700.0, 580.0),
        (685.0, 595.0),
        (685.0, 610.0),
        (770.0, 610.0),
        (795.0, 645.0),
        (720.0, 635.0),
        (760.0, 650.0),
        (475.0, 960.0),
        (95.0, 260.0),
        (875.0, 920.0),
        (700.0, 500.0),
        (555.0, 815.0),
        (830.0, 485.0),
        (1170.0, 65.0),
        (830.0, 610.0),
        (605.0, 625.0),
        (595.0, 360.0),
        (1340.0, 725.0),
        (1740.0, 245.0)]

viajante_berlin52 = Viajante_BL({i:berlin52[i] for i in range(len(berlin52))})

enfriamiento_simulado(viajante_berlin52,1000,0.95,300,300)[1]

# Posible respuesta:
# 7598.442340904538

# La ruta óptima está valorada en 7542.

# Problema pr76
# 76 ciudades (presentado por Padberg y Rinaldi)
# La ruta óptima está valorada en 108159
# La siguiente variable contiene las coordinadas de los lugares. La distancia
# entre ciudades es la euclídea en dos dimensiones.

pr76=[(3600, 2300),
      (3100, 3300),
      (4700, 5750),
      (5400, 5750),
      (5608, 7103),
      (4493, 7102),
      (3600, 6950),
      (3100, 7250),
      (4700, 8450),
      (5400, 8450),
      (5610, 10053),
      (4492, 10052),
      (3600, 10800),
      (3100, 10950),
      (4700, 11650),
      (5400, 11650),
      (6650, 10800),
      (7300, 10950),
      (7300, 7250),
      (6650, 6950),
      (7300, 3300),
      (6650, 2300),
      (5400, 1600),
      (8350, 2300),
      (7850, 3300),
      (9450, 5750),
      (10150, 5750),
      (10358, 7103),
      (9243, 7102),
      (8350, 6950),
      (7850, 7250),
      (9450, 8450),
      (10150, 8450),
      (10360, 10053),
      (9242, 10052),
      (8350, 10800),
      (7850, 10950),
      (9450, 11650),
      (10150, 11650),
      (11400, 10800),
      (12050, 10950),
      (12050, 7250),
      (11400, 6950),
      (12050, 3300),
      (11400, 2300),
      (10150, 1600),
      (13100, 2300),
      (12600, 3300),
      (14200, 5750),
      (14900, 5750),
      (15108, 7103),
      (13993, 7102),
      (13100, 6950),
      (12600, 7250),
      (14200, 8450),
      (14900, 8450),
      (15110, 10053),
      (13992, 10052),
      (13100, 10800),
      (12600, 10950),
      (14200, 11650),
      (14900, 11650),
      (16150, 10800),
      (16800, 10950),
      (16800, 7250),
      (16150, 6950),
      (16800, 3300),
      (16150, 2300),
      (14900, 1600),
      (19800, 800),
      (19800, 10000),
      (19800, 11900),
      (19800, 12200),
      (200, 12200),
      (200, 1100),
      (200, 800)]

viajante_pr76 = Viajante_BL({i:pr76[i] for i in range(len(pr76))})

enfriamiento_simulado(viajante_pr76,200000,0.95,1000,1000)[1]

# Posible respuesta:
# 111378.8272440735

# La ruta óptima está valorada en 108159