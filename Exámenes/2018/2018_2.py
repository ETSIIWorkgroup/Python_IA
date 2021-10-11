# Fichero sin tildes
# INTELIGENCIA ARTIFICIAL - Examen Practico - Enero 2018
# APELLIDOS:
# NOMBRE:
####################################################################################

# ENTREGA:                      SI                 NO

# Representaremos un conjunto de entrenamiento como un diccionario donde las claves
# son tuplas representando instancias y los valores del diccionario son los
# valores de clasificacion.

CE_1 = {('Joven'        ,'NO' , 'Baja'  ): 'Rigida',
        ('Joven'        ,'NO' , 'Normal'): 'Sin_lente',
        ('Joven'        ,'SI' , 'Baja'  ): 'Blanda',
        ('Joven'        ,'SI' , 'Normal'): 'Blanda',
        ('Joven'        ,'SI' , 'Alta'  ): 'Rigida',
        ('Joven'        ,'SI' , 'Normal'): 'Sin_lente',
        ('Prepresbicia' ,'NO' , 'Baja'  ): 'Rigida',
        ('Prepresbicia' ,'NO' , 'Normal'): 'Blanda',
        ('Prepresbicia' ,'NO' , 'Alta'  ): 'Blanda',
        ('Prepresbicia' ,'SI' , 'Alta'  ): 'Sin_lente',
        ('Prepresbicia' ,'SI' , 'Normal'): 'Sin_lente',
        ('Prepresbicia' ,'SI' , 'Baja'  ): 'Sin_lente',
        ('Presbicia'    ,'NO' , 'Baja'  ): 'Blanda',
        ('Presbicia'    ,'NO' , 'Normal'): 'Blanda',
        ('Presbicia'    ,'NO' , 'Alta'  ): 'Rigida',
        ('Presbicia'    ,'SI' , 'Normal'): 'Blanda',
        ('Presbicia'    ,'SI' , 'Baja'  ): 'Sin_lente'}

CE_2 = {('Soleado', 'Alta' , 'Alta'  , 'Debil' ): 'NO',
        ('Soleado', 'Alta' , 'Alta'  , 'Fuerte'): 'NO',
        ('Nublado', 'Alta' , 'Alta'  , 'Debil' ): 'SI',
        ('Lluvia' , 'Suave', 'Alta'  , 'Debil' ): 'SI',
        ('Lluvia' , 'Baja' , 'Normal', 'Debil' ): 'SI',
        ('Lluvia' , 'Baja' , 'Normal', 'Fuerte'): 'NO',
        ('Nublado', 'Baja' , 'Normal', 'Fuerte'): 'SI',
        ('Soleado', 'Suave', 'Alta'  , 'Debil' ): 'NO',
        ('Soleado', 'Baja' , 'Normal', 'Debil' ): 'SI',
        ('Lluvia' , 'Suave', 'Normal', 'Debil' ): 'SI',
        ('Soleado', 'Suave', 'Normal', 'Fuerte'): 'SI',
        ('Nublado', 'Suave', 'Alta'  , 'Fuerte'): 'SI',
        ('Nublado', 'Alta' , 'Normal', 'Debil' ): 'NO',
        ('Lluvia' , 'Suave', 'Alta'  , 'Fuerte'): 'NO'}


CE_3 = {('SI', 'Joven'        ,'NO' , 'Baja'  ):'Rigida',
        ('SI', 'Joven'        ,'NO' , 'Normal'):'Sin_lente',
        ('SI', 'Joven'        ,'SI' , 'Baja'  ):'Blanda',
        ('SI', 'Joven'        ,'SI' , 'Alta'  ):'Rigida',
        ('SI', 'Joven'        ,'SI' , 'Normal'):'Sin_lente',
        ('SI', 'Prepresbicia' ,'SI' , 'Alta'  ):'Sin_lente',
        ('SI', 'Prepresbicia' ,'SI' , 'Normal'):'Sin_lente',
        ('SI', 'Prepresbicia' ,'SI' , 'Baja'  ):'Sin_lente',
        ('SI', 'Presbicia'    ,'NO' , 'Baja'  ):'Blanda',
        ('SI', 'Presbicia'    ,'NO' , 'Normal'):'Blanda',
        ('NO', 'Joven'        ,'NO' , 'Baja'  ):'Rigida',
        ('NO', 'Joven'        ,'NO' , 'Normal'):'Sin_lente',
        ('NO', 'Joven'        ,'SI' , 'Baja'  ):'Blanda', 
        ('NO', 'Joven'        ,'SI' , 'Normal'):'Sin_lente',
        ('NO', 'Prepresbicia' ,'NO' , 'Baja'  ):'Rigida',
        ('NO', 'Prepresbicia' ,'NO' , 'Normal'):'Blanda',
        ('NO', 'Prepresbicia' ,'NO' , 'Alta'  ):'Blanda',
        ('NO', 'Prepresbicia' ,'SI' , 'Alta'  ):'Sin_lente',
        ('NO', 'Prepresbicia' ,'SI' , 'Normal'):'Sin_lente',
        ('NO', 'Prepresbicia' ,'SI' , 'Baja'  ):'Sin_lente',
        ('NO', 'Presbicia'    ,'NO' , 'Baja'  ):'Blanda',
        ('NO', 'Presbicia'    ,'SI' , 'Normal'):'Blanda',
        ('NO', 'Presbicia'    ,'SI' , 'Baja'  ):'Sin_lente'}

CE_4 = {('SI', 'Prepresbicia' ,'NO' , 'Baja'  ):'Rigida',
        ('SI', 'Prepresbicia' ,'NO' , 'Normal'):'Blanda',
        ('SI', 'Prepresbicia' ,'NO' , 'Alta'  ):'Blanda',
        ('SI', 'Presbicia'    ,'NO' , 'Alta'  ):'Rigida',
        ('SI', 'Presbicia'    ,'SI' , 'Normal'):'Blanda',
        ('SI', 'Presbicia'    ,'SI' , 'Baja'  ):'Sin_lente',
        ('NO', 'Joven'        ,'SI' , 'Normal'):'Blanda',
        ('NO', 'Joven'        ,'SI' , 'Alta'  ):'Rigida',
        ('NO', 'Presbicia'    ,'NO' , 'Normal'):'Blanda',
        ('NO', 'Presbicia'    ,'NO' , 'Alta'  ):'Rigida'}


# Una instancia consistente con un conjunto de entrenamiento es una lista de 
# valores de los atributos del conjunto en el orden correspondiente (sin el 
# valor de clasificacion).  Asi, i_a e i_b son instancias consistentes con CE_1

i_a = ('Presbicia', 'SI' , 'Alta')
i_b = ('Joven'    , 'NO' , 'Alta')

# i_c e i_d son instancias consistentes con CE_2

i_c = ('Soleado', 'Suave', 'Alta', 'Fuerte')
i_d = ('Lluvia' , 'Suave', 'Alta', 'Debil' )

# i_e e i_f son instancias consistentes con CE_3 y CE_4

i_e = ('NO', 'Joven' ,'SI' , 'Alta')
i_f = ('SI', 'Joven' ,'SI' , 'Normal')

####################################################################################
# EJERCICIO 1: [1 pto]
# Definir la funcion nb(D,I) que calcule la clasificacion que obtendria la 
# instancia I mediante el metodo de Naive Bayes a partir del conjunto de 
# entrenamiento D. Supondremos siempre que I es una instancia compatible con D. 
# Ejemplo de uso:
# >>> nb(CE_1,i_a)
# 'Blanda'
# >>> nb(CE_2,i_d)
# 'SI'
# >>> nb(CE_3,i_f)
# 'Sin_lente' 
####################################################################################

####################################################################################
# EJERCICIO 2: [1.5 pto]
# Definir la funcion nb_laplace(D,I,k) que calcule la clasificacion que obtendria 
# la instancia I mediante el metodo de Naive Bayes con suavizado de Laplace 
# (usando como parametro k) a partir del conjunto de entrenamiento D. 
# Supondremos siempre que I es una instancia compatible con D. Ejemplo de uso:
# >>> nb_laplace(CE_1,i_b,5)
# 'Rigida'
# >>> nb_laplace(CE_1,i_b,8)
# 'Blanda'
# >>> nb_laplace(CE_3,i_f,10)
# 'Sin_lente'
####################################################################################

####################################################################################
# EJERCICIO 3: [0.5 pto]
# Definir la funcion nbl_mr(Entr,Prueba,k) que calcule la medida de rendimiento
# del metodo Naive Bayes con suavizado de Laplace (usando como parametro k)
# a partir de los conjuntos Entr y Prueba. La funcion debe devolver la proporcion
# de ejemplos de Prueba correctamente clasificados mediante ese metodo
# de aprendizaje usando el conjunto Entr como conjunto de entrenamiento.
# Ejemplo de uso:
# >>> nbl_mr(CE_3,CE_4,5)
# 0.2
# >>> nbl_mr(CE_4,CE_3,5)
# 0.34782608695652173
####################################################################################

####################################################################################
# EJERCICIO 4: [0.5 pto]
# Definir la funcion mejor(Entr,Prueba,Cota) que calcule el valor de k (con k 
# mayor o igual que 1 y k menor que la Cota) tal que para ese valor de k se 
# obtenga la mejor medida de rendimiento del metodo Naive Bayes con suavizado de 
# Laplace usando k como parametro. Si hay varios valores de k para los que se 
# obtenga la mejor medida de rendimiento debe devolver el mayor valor de k. 
# Ejemplo de uso:
#  >>> mejor(CE_3,CE_4,4)
# 3
# >>> mejor(CE_3,CE_4,6)
# 5
# >>> mejor(CE_4,CE_3,10)
# 9
####################################################################################
 

