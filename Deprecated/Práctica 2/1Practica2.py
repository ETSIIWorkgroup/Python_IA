#################################### PRÁCTICA 2 #############################################################################
#
# Técnicas metaheurísticas para optimización
# 
##############################################################################################################################


# Librerias

# 1.- numpy para la representación matricial
import numpy as np

# 2.- random para poder tomar valores aleatorios
import random, math

# 3.- PIL e imageio para leer y escribir imágenes.
from PIL import Image
import imageio

# Para dibujar
import matplotlib as mpl
from matplotlib import pyplot as plt
mpl.rcParams['figure.figsize'] = (15,10) # Para el tamaño de la imagen

# Cargar imágenes

imagen_original = 'gioconda.jpg'
img = Image.open(imagen_original).convert('L')

plt.imshow(img,cmap='gray')

IM2ARRAY = np.array(img)
#IM2ARRAY = np.array(img, dtype='int32')

IM2ARRAY

im2array_shape = IM2ARRAY.shape
#im2array_shape

# Parámetros algoritmos geneticos

# Número de genes que conforman un individuo
NUMERO_DE_GENES = 150

# Tamaño de la población
TAMANO_POB = 500

# Participantes en un torneo
NUM_PARTICIPANTES = 50

# Probabilidad de mutación
PROB_MUTACION = 0.1

# Proporción de individuos que van a ser padres
PROP_CRUCES = 0.5

# Número de iteraciones
ITERACIONES = 10001

# Paso de impresión. Crearemos la imagen correspondiente al mejor individuo después de PASO_IMP iteraciones
PASO_IMP = 100



########### EJERCICIO 1 ################

def genera_gen():
    max_x, max_y = im2array_shape[0] - 1, im2array_shape[1] - 1
    
    x, y = random.randint(0, max_x), random.randint(0, max_y)
    dx, dy = random.randint(0, max_x - x), random.randint(0, max_y - y)
    c = random.randint(0, 255)
    
    return (x, y, dx, dy, c)

# Puedes probar la función
genera_gen()

# Posible respuesta:
# (185, 223, 49, 16, 2)


########### EJERCICIO 2 ################

def genera_individuo():
    return tuple(genera_gen() for _ in range(NUMERO_DE_GENES))

# Ejemplo de uso. Guardamos el individuo generado en la variable ind_1
ind_1 = genera_individuo()
ind_1

# Posible respuesta:
# ((53, 10, 80, 200, 114),
#  (271, 209, 6, 4, 135),
#  ...
#  (310, 220, 35, 19, 174),
#  (264, 121, 37, 45, 200))

def decodifica(ind):
    array_sal = np.zeros(im2array_shape,dtype='uint32')
    array_255 = np.full(im2array_shape,255,dtype='uint32')   
    for (x,y,dx,dy,c) in ind:
        array_sal[x:x+dx,y:y+dy]+= 255 - c
    mini = np.minimum(array_sal,array_255)
    inversa = 255 - mini
    return inversa
    #return inversa.astype('int32')
    
matriz_1 = decodifica(ind_1)
print(matriz_1.tolist())

img_1 = Image.fromarray(matriz_1.astype('uint8'))
plt.imshow(img_1,cmap='gray')

f, axarr = plt.subplots(1,2)
axarr[0].imshow(img,cmap='gray')
axarr[1].imshow(img_1,cmap='gray')


########### EJERCICIO 3 ################


def poblacion_inicial():
    return [genera_individuo() for _ in range(TAMANO_POB)]

def fitness(ind):
    return np.sum(np.absolute(decodifica(ind) - IM2ARRAY))


########### EJERCICIO 4 ################

def selecciona_uno_por_torneo(población, dic):
    min_fit = float('inf')
    
    for _ in range(NUM_PARTICIPANTES):
        random_ind = random.choice(poblacion)
        
        if random_ind in dic:
            fit_ind = dic[random_ind]
        else:
            fit_ind = fitness(random_ind)
            dic[random_ind] = fit_ind
            
        if fit_ind < min_fit:
            min_fit = fit_ind
            min_ind = random_ind
            
    return mind_ind, dic

# Ejemplo de uso
selecciona_uno_por_torneo(poblacion_inicial(),{})


########### EJERCICIO 5 ################

def seleccion_por_torneo(poblacion, num_seleccionados, dic):
    seleccionados = []
    
    for _ in range(num_seleccionados):
        seleccionado, dic = selecciona_uno_por_torneo(poblacion, dic)
        seleccionados.append(seleccionado)
        
    return seleccionados, dic

# Ejemplo de uso
seleccion_por_torneo(poblacion_inicial(),4,{})


########### EJERCICIO 6 ################

def cruza(i1, i2):
    cruce = random.randrange(1, len(i1))
    
    return [i1[:cruce] + i2[cruce:], i2[:cruce] + i1[cruce:]]


########### EJERCICIO 7 ################

def cruza_padres(padres):
    return [hijo for i in range(0, len(padres), 2) for hijo in cruza(padres[i],padres[i+1])]


########### EJERCICIO 8 ################

def muta(ind):
    if random.random() <= PROB_MUTACION:
        i = random.randrange(NUMERO_DE_GENES)
        ind = ind[:i] + (genera_gen(),) + ind[i+1:]
        
    return ind


########### EJERCICIO 9 ################

def muta_individuos(poblacion):
    return [muta(ind) for ind in poblacion]


########### EJERCICIO 10 ################

def nueva_generacion(poblacion, n_padres, n_directos, dic):
    padres, dic = seleccion_por_torneo(poblacion, n_padres, dic)
    directos, dic = seleccion_por_torneo(poblacion, n_directos, dic)
    
    hijos_mut = muta_individuos(cruza_padres(padres))
    
    return dic, directos + hijos_mut

def algoritmo_genetico():
    poblacion= poblacion_inicial()
    dic = {}
    n_padres = round(TAMANO_POB * PROP_CRUCES)
    n_padres = (n_padres if n_padres%2==0 else n_padres-1)
    n_directos = TAMANO_POB - n_padres
    mejores = []
    for counter in range(ITERACIONES):
        if counter%PASO_IMP == 0:
            print(counter)
            nuevo_dic = {}
            actual = 'inicial'
            min = float('inf')
            for ind in poblacion:
                f_ind = fitness(ind)
                nuevo_dic[ind] = f_ind
                if f_ind < min:
                    actual = ind
                    min = f_ind
            img_mejor = decodifica(actual).astype('uint8')
            imageio.imwrite('ga_{:>08}.jpg'.format(counter//PASO_IMP),img_mejor)
            mejores.append(min)
            dic, poblacion = nueva_generacion(poblacion,n_padres,n_directos,dic)
        else:
            dic, poblacion = nueva_generacion(poblacion,n_padres,n_directos,dic)
            print('.',end='')
    return mejores

sal_ag = algoritmo_genetico()

plt.plot(sal_ag[1:])
plt.show()
