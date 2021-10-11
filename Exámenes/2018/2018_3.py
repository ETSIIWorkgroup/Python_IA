# INTELIGENCIA ARTIFICIAL - Examen Practico - Diciembre 2018
# APELLIDOS:
# NOMBRE:
#######################################################################

#   ENTREGA:             SI                  NO

import math

# Representaremos un conjunto de entrenamiento como una lista de
# instancias y una instancia es un diccionario de pares atributo:valor.
# En estos ejercicios consideraremos siempre que el atributo de clasificación
# es "Clasif" y que toma los valores "SI" y "NO". Por ejemplo

CE1 = [{"Edad":"Joven",        "Diagnóstico":"Miope",        "Astigmatismo":"NO", "Lágrima":"Reducida", "Clasif":"SI" },
       {"Edad":"Joven",        "Diagnóstico":"Miope",        "Astigmatismo":"NO", "Lágrima":"Normal",   "Clasif":"NO"  },
       {"Edad":"Joven",        "Diagnóstico":"Miope",        "Astigmatismo":"SI", "Lágrima":"Reducida", "Clasif":"SI" },
       {"Edad":"Joven",        "Diagnóstico":"Miope",        "Astigmatismo":"SI", "Lágrima":"Normal",   "Clasif":"NO"  },
       {"Edad":"Joven",        "Diagnóstico":"Hipermétrope", "Astigmatismo":"NO", "Lágrima":"Reducida", "Clasif":"SI" },
       {"Edad":"Joven",        "Diagnóstico":"Hipermétrope", "Astigmatismo":"NO", "Lágrima":"Normal",   "Clasif":"NO"  },
       {"Edad":"Joven",        "Diagnóstico":"Hipermétrope", "Astigmatismo":"SI", "Lágrima":"Reducida", "Clasif":"SI" },
       {"Edad":"Joven",        "Diagnóstico":"Hipermétrope", "Astigmatismo":"SI", "Lágrima":"Normal",   "Clasif":"NO"  },
       {"Edad":"PrePresbicia", "Diagnóstico":"Miope",        "Astigmatismo":"NO", "Lágrima":"Reducida", "Clasif":"SI" },
       {"Edad":"PrePresbicia", "Diagnóstico":"Miope",        "Astigmatismo":"NO", "Lágrima":"Normal",   "Clasif":"NO"  },
       {"Edad":"PrePresbicia", "Diagnóstico":"Miope",        "Astigmatismo":"SI", "Lágrima":"Reducida", "Clasif":"SI" }, 
       {"Edad":"PrePresbicia", "Diagnóstico":"Miope",        "Astigmatismo":"SI", "Lágrima":"Normal",   "Clasif":"NO"  },
       {"Edad":"PrePresbicia", "Diagnóstico":"Hipermétrope", "Astigmatismo":"NO", "Lágrima":"Reducida", "Clasif":"SI" },
       {"Edad":"PrePresbicia", "Diagnóstico":"Hipermétrope", "Astigmatismo":"NO", "Lágrima":"Normal",   "Clasif":"NO"  },
       {"Edad":"PrePresbicia", "Diagnóstico":"Hipermétrope", "Astigmatismo":"SI", "Lágrima":"Reducida", "Clasif":"SI" },
       {"Edad":"PrePresbicia", "Diagnóstico":"Hipermétrope", "Astigmatismo":"SI", "Lágrima":"Normal",   "Clasif":"SI" },
       {"Edad":"Presbicia",    "Diagnóstico":"Miope",        "Astigmatismo":"NO", "Lágrima":"Reducida", "Clasif":"SI" },
       {"Edad":"Presbicia",    "Diagnóstico":"Miope",        "Astigmatismo":"NO", "Lágrima":"Normal",   "Clasif":"SI" },
       {"Edad":"Presbicia",    "Diagnóstico":"Miope",        "Astigmatismo":"SI", "Lágrima":"Reducida", "Clasif":"SI" },
       {"Edad":"Presbicia",    "Diagnóstico":"Miope",        "Astigmatismo":"SI", "Lágrima":"Normal",   "Clasif":"NO"  },
       {"Edad":"Presbicia",    "Diagnóstico":"Hipermétrope", "Astigmatismo":"NO", "Lágrima":"Reducida", "Clasif":"SI" },
       {"Edad":"Presbicia",    "Diagnóstico":"Hipermétrope", "Astigmatismo":"NO", "Lágrima":"Normal",   "Clasif":"NO"  },
       {"Edad":"Presbicia",    "Diagnóstico":"Hipermétrope", "Astigmatismo":"SI", "Lágrima":"Reducida", "Clasif":"SI" },
       {"Edad":"Presbicia",    "Diagnóstico":"Hipermétrope", "Astigmatismo":"SI", "Lágrima":"Normal",   "Clasif":"SI" }]

CE2 = [{"Cielo":"Soleado", "Temperatura":"Alta",        "Humedad":"Alta",    "Viento":"Débil",  "Clasif":"NO" },
       {"Cielo":"Soleado", "Temperatura":"Alta",        "Humedad":"Alta",    "Viento":"Fuerte", "Clasif":"NO" },
       {"Cielo":"Nublado", "Temperatura":"Alta",        "Humedad":"Alta",    "Viento":"Débil",  "Clasif":"SI" },
       {"Cielo":"Lluvia",  "Temperatura":"Suave",       "Humedad":"Alta",    "Viento":"Débil",  "Clasif":"SI" },
       {"Cielo":"Lluvia",  "Temperatura":"Baja",        "Humedad":"Normal",  "Viento":"Débil",  "Clasif":"SI" },
       {"Cielo":"Lluvia",  "Temperatura":"Baja",        "Humedad":"Normal",  "Viento":"Fuerte", "Clasif":"NO" },
       {"Cielo":"Nublado", "Temperatura":"Baja",        "Humedad":"Normal",  "Viento":"Fuerte", "Clasif":"SI" },
       {"Cielo":"Soleado", "Temperatura":"Suave",       "Humedad":"Alta",    "Viento":"Débil",  "Clasif":"NO" },
       {"Cielo":"Soleado", "Temperatura":"Baja",        "Humedad":"Normal",  "Viento":"Débil",  "Clasif":"SI" },
       {"Cielo":"Lluvia",  "Temperatura":"Suave",       "Humedad":"Normal",  "Viento":"Débil",  "Clasif":"SI" },
       {"Cielo":"Soleado", "Temperatura":"Suave",       "Humedad":"Normal",  "Viento":"Fuerte", "Clasif":"SI" },
       {"Cielo":"Nublado", "Temperatura":"Suave",       "Humedad":"Alta",    "Viento":"Fuerte", "Clasif":"SI" },
       {"Cielo":"Nublado", "Temperatura":"Alta",        "Humedad":"Normal",  "Viento":"Débil",  "Clasif":"SI" },
       {"Cielo":"Lluvia",  "Temperatura":"Suave",       "Humedad":"Alta",    "Viento":"Fuerte", "Clasif":"NO" }] 

CE3 = [{"Color":"Rojo", "Forma":"Cuadrado","Tamaño":"Grande",   "Clasif":"SI"},
             {"Color":"Azul",  "Forma":"Cuadrado","Tamaño":"Grande",   "Clasif":"SI"},
             {"Color":"Rojo",  "Forma":"Redondo", "Tamaño":"Pequeño","Clasif":"NO"},
             {"Color":"Verde","Forma":"Cuadrado","Tamaño":"Pequeño","Clasif":"NO"},
             {"Color":"Rojo",  "Forma":"Redondo", "Tamaño":"Grande",    "Clasif":"SI"},
             {"Color":"Verde","Forma":"Cuadrado","Tamaño":"Grande",   "Clasif":"NO"}]


#######################################################################
# Ejercicio 1 [1 pto]:
# Define la función entropia(C) que devuelva la entropia del conjunto de
# entrenamiento C. Si C está vacío, la entropía debe ser 0. Si todos son valores
# positivos o todos negativos, la entropía debe ser cero. Ejemplo de uso:
# >>> entropia(CE1)
#         0.9544340029249649
# >>> entropia(CE2)
#        0.9402859586706309
# >>> entropia(CE3)
#        1.0
#######################################################################

#######################################################################
# Ejercicio 2 [1 pto]:
# Define la funcion mejor(C) que tome un conjunto de entrenamiento
# y devuelva el mejor atributo para ponerlo en la raíz del aŕbol
# en el algoritmo ID3. En caso de igualdad de condiciones,
# cualquier atributo candidato se considerará válido. Ejemplo de uso:
# >>> mejor(CE1)
#         'Astigmatismo'
# >>> mejor(CE2)
#         'Temperatura'
# >>> mejor(CE3)
#         'Forma'
#######################################################################

#######################################################################
# EJERCICIO 3: [1 pto]
# En este ejercicio, se define una regla como un diccionario donde una 
# de las claves es "Clasif" y representa la conclusión y el resto de 
los pares Atrib:Valor representan las
# condiciones de la regla. Por ejemplo:

# Si Astigmatismo = SI y Lágrima = Normal entonces Clasif  = NO
R1 = {"Astigmatismo":"SI", "Lágrima":"Normal","Clasif":"NO"}

# Si (vacío) entonces Clasif = NO
R2 = {"Clasif":"NO"}

# Si (vacío) entonces Clasif = SI
R3 = {"Clasif":"SI"}

# Si Cielo=Soleado y Humedad=Alta entonces Clasif = SI
R4 = {"Cielo":"Soleado","Humedad":"Alta","Clasif":"SI"}

# Si Cielo = Lluvia y Temperatura= Alta y Humedad=Normal entonces Clasif=SI
R5 = {"Cielo":"Lluvia","Temperatura":"Alta","Humedad":"Normal","Clasif":"SI"}

# Define la función fr(R,C) que devuelva la frecuencia relativa de la regla R
# sobre el conjunto de entrenamiento C. Si la regla no cubre ningún ejemplo,
# el valor de la frecuencia relativa debe ser cero.
# Ejemplo de uso:
#  >>> fr(R1,CE1)
#         0.6666666666666666
# >>> fr(R2,CE2)
#         0.35714285714285715
# >>> fr(R3,CE3)
#         0.5
#######################################################################

#######################################################################
# EJERCICIO 4: [1 pto]
# Decimos que una instancia es compatible con un conjunto de entrenamiento
# si es un diccionario que asigna valores a todos los atributos de las
# condiciones del conjunto de entrenamiento. Por ejemplo

i1 = {"Edad":"Presbicia", "Diagnóstico":"Miope", "Astigmatismo":"SI", "Lágrima":"Reducida"}

i2 = {"Cielo":"Soleado", "Temperatura":"Suave", "Humedad":"Alta", "Viento":"Fuerte"}

# Definir la funcion nb(D,I) que calcule la clasificacion que
# obtendria la instancia I mediante el metodo de Naive Bayes a partir
# del conjunto de entrenamiento D. Supondremos siempre que I es una
# instancia compatible con D. Recuerda que suponemos que el
# atributo de clasificación es "Clasif" y que los únicos valores que
# puede tomar son "SI" y "NO". Ejemplo de uso:
# >>> nb(CE1,i1)
#         'SI'
# >>> nb(CE2,i2)
#         'NO'
#######################################################################


