# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 18:48:23 2015

@author: Lin
"""

import numpy as np

#n elementos
#m mochilas
#indiv numero de individiuos
def genFirst(indiv, n, m):
    aux = [np.random.randint(m,size=n)]
    first = np.array(aux)
 
    for k in xrange(indiv - 1):
        aux = [np.random.randint(m + 1,size=n) ]
        first = np.append(first,aux,axis = 0) 
    return  first
   
#genFirst(10,4,7)
   
   
def mutation(indiv,N):
    mutateGen = np.random.randint(N)
    indiv[mutateGen] = np.random.randint(N)    
    return indiv
    
#a = [0,2,4,5]
#mutation(a,4)

def reproduction(indiv1,indiv2,N):
    indivAux = indiv1
    indiv1 = indiv1[:N / 2] + indiv2[(N / 2) :]
    indiv2 = indiv2[:N / 2] + indivAux[(N / 2) :]
    print indiv1, indiv2

def correction(indiv,mapIndiv,proff,weig,orgCap):
    q = []    
    for key in mapIndiv.keys():
        for element in mapIndiv[key]:
            q.append((proff[key][element]/weig[key][element],element))
    
    s = sorted(q, key = lambda ar: ar[0])
    print s    
     
#a = [1,2,3,4]
#b = [5,6,7,8]

#reproduction(a,b,4)