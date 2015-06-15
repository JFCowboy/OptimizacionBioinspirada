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

'''

'''
def evaluateInd( indiv ):
    obj = [0]*(M+1)
    repetir = True
    while ( repetir ):
        capacidades = np.copy(cap)
        for elemento in xrange( N ):
            mochila = indiv[ elemento ] 
            if( mochila != M ):
                obj[ mochila ] += prof[ mochila ][ elemento ]
                capacidades[ mochila ] -= w[ elemento ]
    
        #print "CAP:", capacidades, "OBJ:", obj
        #Poner restricciones y que este dentro de los rangos
        tam = len( capacidades )
        noValid = [ idx for idx in xrange( tam ) if capacidades[idx]<0 ]
        print noValid
        if( len(noValid)>0 ):
            indiv = correction( indiv, noValid, prof, w, cap, capacidades)
        else:
            repetir = False;
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
    res = []
    
    for ind in indiv:
        evalInd = [evaluateInd(ind)]
        #print "INDIVIDUO: ",ind, evalInd
        if( len(res) == 0 ):
            res = np.array(evalInd)
        else:
            res = np.append(res, evalInd, axis=0)
        
    return res
    