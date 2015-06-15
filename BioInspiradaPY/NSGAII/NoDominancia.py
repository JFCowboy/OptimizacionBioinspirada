# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 03:04:48 2015

@author: Lin
"""

def toFloat(s):
    try:
        return float(s)
    except:
        return s
def compareVal1(val1,val2):
    for v in xrange( len( val1 ) ):
        if(val1[v] > val2[v]):
            return False
    for v in xrange( len( val1 )):
        if(val1[v] < val2[v]):
            return True 
    return False

def compareVal2(val1,val2):
    for v in xrange( len( val1 ) ):
        if(val1[v] < val2[v]):
            return False
    for v in xrange( len( val1 )):
        if(val1[v] > val2[v]):
            return True 
    return False
        
def noDominancia(z,N):        

    s = []
    n = []
    F = []
    indiv = [0]*N  
    for k, val1 in enumerate(z):
        s.append(set())
        n.append(0)
        for j, val2 in enumerate(z):
            if(j == k):
                continue
            if(compareVal1(val1,val2)):
                s[k].add(j)
            elif (compareVal2(val1,val2)):
                n[k] += 1
        if n[k] == 0:
            F.append(set())
            F[0].add(k)
    
    fc = 0
    #print "F->->->", F
    while (len(F[fc])!= 0):
        Q = set()
        for k in F[fc]:
            #print k
            for j in s[k]:
                n[j] -= 1
                if (n[j] == 0):
                    Q.add(j)
        fc += 1   
        #print "Q ->", Q
        if fc >= len(F):
            F.append(set())
        F[fc] = Q

        #print "F ->",F
        
        idx = 0
        for k in F:
            
            for i in k:
                indiv[i] = idx
            idx += 1
        
    return indiv