'''
Created on 14/06/2015

@author: JuanFelipe, Lin
'''
import numpy as np
from FirstGen import genFirst
from Evaluate import evaluate
from NoDominancia import noDominancia
from CrowdingDistance import crowdinDistance
from GenChild import genChild, genChild2

n = 10
m = 2
inv = 30
nIter = 100
probMutar = 30
'''
pf = np.array([np.random.randint(100, size=n) for x in xrange(m)])
cc = np.random.randint(20, 50, size=m)
ww = np.random.randint(1, 50, size=n)
'''
pg = genFirst(inv, n, m)

'''caso1
pf =[[71, 54 ,41, 99,  4, 40, 91, 68, 14, 63],
     [19, 21, 55,  0, 90, 48, 40, 80, 58, 26]]
cc = [20 , 25]
ww = [23, 11, 20,  2, 46, 36, 39, 31, 24, 21] 
'''
#''' caso2
pf =[[1, 1, 1, 0,  1, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 1,  0, 1, 1, 1, 1, 1, 1]]
cc = [2 , 2]
ww = [1, 1, 1, 1, 1, 1, 1, 1, 1,1]

print "PG:",pg, "WW:",ww, "CC:",cc, "PF:",pf
evalu, pg = evaluate(pg, pf, ww, cc, n, m)
pareto,setsPareto = noDominancia(evalu, inv)
#print "Paretto ->",  pareto
#print evaluate(pg, pf, ww, cc, n, m)
crow = crowdinDistance(n, m, pg, pf, cc)
#print crow
Qt = genChild(pg, pareto, crow, n, m, probMutar)

for idx in xrange( nIter ):
    print "Generacion %d" % (idx)
    
   
    R = np.append(pg,Qt, axis = 0) 
    #print "R ->", R
    F,setsF = noDominancia(R, len(R))
    crowDis = crowdinDistance(n, m, R, pf, cc)
    
    idx = 0
    pt_1 = []
    for k in setsF:
        if(len(pt_1) + len(k) <= inv):
            for i in k:
                if(len(pt_1) == 0):
                    pt_1 = np.array([R[i]])
                else:
                    pt_1 = np.append(pt_1, [R[i]], axis = 0)
            idx += 1
        else:
            aux = [(index, crowDis[index]) for index in k]
            aux = sorted(aux, key = lambda ar: ar[1])
            for j in aux:
                if(len(pt_1) >= inv):
                    break
                if(len(pt_1) == 0):
                    pt_1 = np.array([R[j[0]]])
                else:
                    pt_1 = np.append(pt_1,[R[j[0]]], axis = 0)
            break
    pg = pt_1
    
    evalu, pg = evaluate(pg, pf, ww, cc, n, m)
    pareto,setsPareto = noDominancia(evalu, inv)
    #print "Paretto ->",  pareto
    #print evaluate(pg, pf, ww, cc, n, m)
    crow = crowdinDistance(n, m, pg, pf, cc)
    Qt = genChild2(pg, pareto, crow, n, m, probMutar)
    
    print "Funcion ->", evalu
    #print setsF
print pt_1
print evaluate(pt_1, pf, ww, cc, n, m)
    #print Qt