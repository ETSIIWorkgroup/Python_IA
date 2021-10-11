###############################################################################
# Apellidos y nombre:
# DNI:
###############################################################################

# Fichero sin tildes

# INTELIGENCIA ARTIFICIAL - 22 de noviembre 2017
# Examen practico

# Entrega              SI             NO

###############################################################################
# En los siguientes ejercicios vamos a implementar algunas funciones
# relacionadas con el clustering jerarquico aglomerativo generado a partir de 
# una lista de elementos. Adoptaremos las siguientes definiciones:
# - Un cluster es una lista no vacia ordenada (con sorted) de elementos
# - Una particion de una lista ordenada (con sorted) de clusters de manera que
#   todo elemento este en alguno de los clusters.
# - Dada una lista de elementos [e0,...,e(n-1)] llamaremos matriz de distancias 
#   asociada a una lista MD = [l0,l1,...,l(n-1)] donde cada li es una lista de n 
#   elementos li = [li_0,li_1,...,li_(n-1)] y cada elemento li_j es la distancia 
#   del elemento 'ei' hasta 'ej'. Por ejemplo, si consideramos los elementos

elem_1 = ['a0','a1','a2','a3']

# una posible matriz de distancias asociada a esa particion puede ser

MD_1 = [[0,6,7,5],
        [6,0,1,1],
        [7,1,0,7],
        [5,1,7,0]]

# donde la distancia entre 'a0' y 'a2' es 7 y la distancia entre 'a1' y 'a3' es 1.
# Otro ejemplo de lista de elementos y matriz asociada es el siguiente 

elem_2 = ['al','ca','co','gr','hu','ja','ma','se']

MD_2 = [[ 0,1,2,3,4,5,6,7],
        [ 1,0,4,6,1,2,3,5],
        [ 2,4,0,1,2,3,5,7],
        [ 3,6,1,0,3,5,7,8],
        [ 4,1,2,3,0,7,8,3],
        [ 5,2,3,5,7,0,3,5],
        [ 6,3,5,7,8,3,0,3],
        [ 7,5,7,8,3,5,3,0]]

# donde la distancia entre 'ca' y 'co' es 4 y la distancia entre
# 'ma' y 'se' es 3. 

#################################################################################
# EJERCICIO 1 [0.5 ptos.]:
# Dados dos clusters C1 y C2, se define la 'distancia central' entre C1 y C2 como la 
# distancia media entre todos los pares de elementos donde uno de ellos pertenece a C1 
# y el otro a C2. Por ejemplo, si C1 = ['hu','ca','ma'] y C2 = ['se','co'] entonces 
# la distancia central de C1 y C2 se calcula haciendo la media entre las seis (3 x 2) 
# distancias entre los pares de objetos. Se pide definir dist_cen(C1,C2,MD,Lista) 
# donde C1 y C2 son clusters, MD es una matriz de distancias y Lista es la lista de 
# todos los elementos del problema. Ejemplo de uso:
#     >>> dist_cent(['a0','a1'],['a2'],MD_1,elem_1)
#         4.0
#     >>> dist_cent(['hu','ca','ma'],['se','co'],MD_2,elem_2)
#         3.6666666666666665
#################################################################################

#################################################################################
# EJERCICIO 2 [1 pto.]:
# En el algoritmo de clusterng jerarquico aglomerativo agrupamos los pares de
# clusters que esten a distancia minima. En este ejercicio, se pide definir
# una funcion prox(LC,MD,LE) que tome como entrada una lista de clusters LC,
# una matriz de distancias MD y la lista de elementos del problema LE y devuelva 
# un par [D,P] donde D es la distancia minima a la que se encuentran dos clusters
# de LC y P es la lista de pares de clusters [C1,C2] tales que se encuentran
# a distancia D. Para evitar pares duplicados (por ejemplo, [C1,C2] y [C2,C1])
# solo aceptaremos pares [C1,C2] tales que C1 aparezca antes que C2 en la lista LC.
# Ejemplo de uso:
#    >>> prox([['a0'],['a1'],['a2'],['a3']],MD_1,elem_1)
#        [1.0, [[['a1'], ['a2']], [['a1'], ['a3']]]]
#    >>> prox([['al','ca'],['co','gr','hu'],['se','ja']],MD_2,elem_2)
#        [3.3333333333333335, [[['al', 'ca'], ['co', 'gr', 'hu']]]]
#################################################################################

#################################################################################
# EJERCICIO 3 [0.5 ptos.]:
# Si los clusters C1 y C2 estan a distancia minima y C1 y C3 tambien estan a
# distancia minima debemos decidir si unimos C1 a C2 o lo unimos con C3. Para
# solucionar este problema se pide definir la funcion auxiliar limpia(L1) que
# tome como entrada una lista de pares L1 y devuelva una lista de pares L2
# formada a partir de L1 del siguiente modo:
# - Recorremos la lista L1 de izquierda a derecha.
# - Para cada par P de L1, si ninguno de los elementos del par P pertenece a un par
#   que ya hayamos puesto en L2, entonces ponemos P en L2.
# - Si alguno de los elementos de P pertenece a un par de L2, entonces no ponemos 
#    P en L2.
# Ejemplo de uso
#  >>> limpia([[1,2],[5,6],[1,3],[6,7],[4,8]])
#      [[1, 2], [5, 6], [4, 8]]
#################################################################################

#################################################################################
# EJERCICIO 4 [1.5 ptos]:
# Por ultimo definir la funcion dendrograma(L,MD) que reciba una lista de elementos
# L y una matriz de distancias MD y devuelba una lista de particiones
# [P0,P1,...,Pk] donde la primera particion es una particion formada por todos los
# clusters individuales que se pueden formar a partir de la lista de elementos L
# y la ultima particion contenga un unico cluster con todos los elementos.
# Para pasar de Pi a P(i+1) uniremos todos los pares de clusters de Pi que esten a
# distancia minima. Si un cluster C1 esta a distancia minima de C2 y de C3, tomaremos el
# par [C1,C2] en lugar de [C1,C3] usando la funcion limpica del ejercicio anterior.
# Ejemplo de uso:
#   >>> dendrograma(elem_1,MD_1)
#       [[['a0'], ['a1'], ['a2'], ['a3']],
#        [['a0'], ['a1', 'a2'], ['a3']],
#        [['a0'], ['a1', 'a2', 'a3']],
#        [['a0', 'a1', 'a2', 'a3']]]
#   >>> dendrograma(elem_2,MD_2)
#        [[['al'], ['ca'], ['co'], ['gr'], ['hu'], ['ja'], ['ma'], ['se']],
#         [['al', 'ca'], ['co', 'gr'], ['hu'], ['ja'], ['ma'], ['se']],
#         [['al', 'ca', 'hu'], ['co', 'gr'], ['ja'], ['ma'], ['se']],
#         [['al', 'ca', 'hu'], ['co', 'gr'], ['ja', 'ma'], ['se']],
#         [['al', 'ca', 'co', 'gr', 'hu'], ['ja', 'ma'], ['se']],
#         [['al', 'ca', 'co', 'gr', 'hu'], ['ja', 'ma', 'se']],
#         [['al', 'ca', 'co', 'gr', 'hu', 'ja', 'ma', 'se']]]
#################################################################################
