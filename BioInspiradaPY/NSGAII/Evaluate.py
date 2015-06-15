'''
Created on 14/06/2015

@author: JuanFelipe, Lina Rosales
'''
import numpy as np 
from numpy.matlib import zeros
#from FirstGen import correction

prof = [[]]
w    = []
cap  = []
N    =0
M    =0; 

'''

'''


def correction(indiv,mapIndiv,proff,weig,orgCap, cap):
    global M
    q = []
#    print "proffit -> ", proff    
#    print "weig -> ", weig
#    print "MapIndiv ->", mapIndiv
    for key in mapIndiv.keys():
        for element in mapIndiv[key]:
#            print "q ->", proff[key][element],"--", weig[element]
            q.append((key,proff[key][element]*1.0/weig[element],element))
            
    #print "Individuo Inicial ->", indiv     
    qSort = sorted(q, key = lambda ar: (ar[0],ar[1]))
    lastQ = -1    
    for s in qSort:
        if(s[0] != lastQ):
            indiv[s[2]] = M
        lastQ = s[0]
        
   
    #print "Sorted ->", qSort 
    #print "Individuo Final ->", indiv 
    return indiv
    
def evaluateInd( indiv ):
    obj = [0]*(M)
    repetir = True
    while ( repetir ):
        capacidades = np.copy(cap)
        for elemento in xrange( N ):
            mochila = indiv[ elemento ] 
            if( mochila != M ):
                obj[ mochila ] += prof[ mochila ][ elemento ]
                capacidades[ mochila ] -= w[ elemento ]
    
        
        #Poner restricciones y que este dentro de los rangos
        tam = len( capacidades )
        noValid = [ idx for idx in xrange( tam ) if capacidades[idx]<0 ]
<<<<<<< HEAD
        objNoValid = {}
        
        for idx in xrange( len(indiv)):
             x = indiv[idx]
             if(x in noValid):
                 if(x not in objNoValid):
                     objNoValid[x] = []
                 objNoValid[x].append( idx )
        
        #print "NoValid ->",noValid
        #print "ObjNoValid ->", objNoValid
=======
        #print "Individuo",indiv
        #print "NOVALID", noValid, capacidades
        objNoValid = {}
        for idx in xrange( len(indiv) ):
            x = indiv[idx]
            if( x in noValid ):
                if( x not in objNoValid ):
                    objNoValid[ x ] = []
                objNoValid[x].append( idx )
        
        #print "Objeto no valido",objNoValid
        
        print noValid
>>>>>>> origin/master
        if( len(noValid)>0 ):
            indiv = correction( indiv, objNoValid, prof, w, cap, capacidades)
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
    