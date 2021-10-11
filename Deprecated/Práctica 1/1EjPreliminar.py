#################################### EJEMPLO DE FUERZA BRUTA #################################################
#
# Se pide definir una clase Viajante_n, que sirva para definir un problema del viajante generado 
# aleatoriamente con n ciudades. El constructor de la clase recibe un valor 𝑛 que indicará el número 
# de ciudades y un parámetro 𝑒𝑠𝑐𝑎𝑙𝑎. Las coordenadas 𝑥 e 𝑦 de cada ciudad se tomaran aleatoriamente 
# en el rango [−𝑒𝑠𝑐𝑎𝑙𝑎,+𝑒𝑠𝑐𝑎𝑙𝑎].
#
##############################################################################################################


# Librerias
import random, time, math
from itertools import permutations

# Clase Viajante_n()
class Viajante_n():
    
    def __init__(self, n, escala):
        self.ciudades = list(range(1, n+1))
        self.coordenadas = {ciudad : (random.uniform(-escala, escala), random.uniform(-escala, escala)) for ciudad in self.ciudades}
    
    def distancia(self, c1, c2):
        coordenadas1 = self.coordenadas[c1]
        coordenadas2 = self.coordenadas[c2]
        return math.sqrt(((coordenadas1[0] - coordenadas2[0]) **2) + ((coordenadas1[1] - coordenadas2[1]) **2))
            
    def distanciaCircuito(self, listaCiudades): 
        return sum(self.distancia(listaCiudades[ciudad], listaCiudades[ciudad+1]) for ciudad in range (len(listaCiudades) - 1)) + self.distancia(listaCiudades[-1],listaCiudades[0])
    

# Algunos ejemplos:
pv5 = Viajante_n(5,3)
print("Ciudades pv5: {}".format(pv5.ciudades))
print("Coordenadas pv5: {}".format(pv5.coordenadas))      
circuito5=[3,1,4,5,2]
print("Distancia recorrida circuito {}: {}".format(circuito5, pv5.distanciaCircuito(circuito5)))
print("\n")

# ------------------------------------------

pv7 = Viajante_n(7,6)
print("Ciudades pv7: {}".format(pv7.ciudades))
print("Coordenadas pv7: {}".format(pv7.coordenadas))      
circuito7=[6,1,7,2,4,3,5]
print("Distancia recorrida circuito {}: {}".format(circuito7, pv7.distanciaCircuito(circuito7)))
print("\n")


# Optimización del problema del viajante: 
def optimizacionViajante(pv):
    tiempoInicio = time.time()
    posiblesRutas = permutations(pv.ciudades)
    minimaDistancia = float("inf")
    for ruta in posiblesRutas:
        distanciaActual = pv.distanciaCircuito(ruta)
        if distanciaActual < minimaDistancia:
            minimaDistancia = distanciaActual
            minimaRuta = ruta
    tiempoTotal = time.time() - tiempoInicio
    print("Tiempo empleado: " + str(tiempoTotal) + " segundos.")
    return minimaRuta, minimaDistancia


# Algunos ejemplos:
optimizacionViajante(pv5)

optimizacionViajante(pv7)

pv8 = (8, 40)
print("Ciudades pv8: {}".format(pv8.ciudades))
print("Coordenadas pv8: {}".format(pv8.coordenadas))      
circuito8=[3,1,4,5,2,6,7,8]
print("Distancia recorrida circuito {}: {}".format(circuito8, pv8.distanciaCircuito(circuito8)))
print("\n")
optimizacionViajante(pv8)

pv9 = (9, 40)
print("Ciudades pv9: {}".format(pv9.ciudades))
print("Coordenadas pv9: {}".format(pv9.coordenadas))      
circuito9=[6,1,7,2,4,3,5,9,8]
print("Distancia recorrida circuito {}: {}".format(circuito9, pv9.distanciaCircuito(circuito9)))
print("\n")
optimizacionViajante(pv9)
    