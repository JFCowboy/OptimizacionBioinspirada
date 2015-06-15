'''
Created on 15/06/2015

@author: JuanFelipe, Lin
'''

import numpy as np


def Valor( obj, indiv, prof):
    res = 0;
    for idx, x in enumerate( indiv ):
        if( x==obj ):
            res += prof[obj][idx]
    return res
    
'''
'''
def crowdinDistance(N, M, indiv, profit, constrain):
    INF = float("inf")
    tam = len( indiv )
    crowDist = [0]*tam
    for idx in xrange( M ):
        I = [ (id, Valor(idx, indiv[id], profit) ) for id in xrange(tam)  ]
        Is= sorted( I, key=lambda a: a[1] )
        crowDist[ Is[0][0] ] = INF 
        crowDist[ Is[tam-1][0] ] = INF
        
        for j in xrange(2, tam-1):
            crowDist[ Is[j][0] ] += (Is[j+1][1]-Is[j-1][1])*1.0/(constrain[idx]);
    
    return crowDist 