'''
Created on 14/06/2015

@author: JuanFelipe, Lina Rosales
'''

import numpy as np 
from numpy.matlib import zeros

prof = [[]]
w    = []
cap  = []
N    =0
M    =0; 

def evaluateInd( indiv ):
    obj = zeros(M+1)
    
    capacidades = np.copy(cap)
    for elemento in xrange( N ):
        mochila = indiv[ elemento ] 
        if( mochila != 0 ):
            obj[ mochila ] += prof[ mochila ][ elemento ]
            capacidades[ mochila ] -= w[ elemento ]
    
    #Poner restricciones y que este dentro de los rangos
    
    #
    return obj
'''
Arguments
    indiv:       individuos a calcularle el fitness
    profits:     Matriz MxN de  ganancia de usa el elemento i en la mochila j
    weigth:      Vector de peso de usar el elemento i
    capacidades: Maxima capacidad de cada mochila j
    N: numero de elementos
    M: numero de mochilas
Return
    obj:
    
funcion que evalua para un individuo el fitnes los elementos vs mochials
'''
def evaluate( indiv, profits, weigth, capacidades, n, m ):
    global prof, w, cap, N, M 
    prof = profits
    w = weigth
    cap = capacidades
    N = n
    M = m
     
    for ind in indiv:
        print ind

lim = 2
ww = np.array([np.random.randint(100, size=10) for x in xrange(lim)])
cc = np.random.randint(150, size=10)
print ww, cc

    