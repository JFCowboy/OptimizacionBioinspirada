'''
Created on 14/06/2015

@author: JuanFelipe, Lin
'''
import numpy as np
from FirstGen import genFirst
from Evaluate import evaluate
from NoDominancia import noDominancia


n = 10
m = 3
inv = 20


pf = np.array([np.random.randint(100, size=n) for x in xrange(m)])
cc = np.random.randint(20, 50, size=m)
ww = np.random.randint(50, size=n)
pg = genFirst(inv, n, m)

#print "PG:",pg, "WW:",ww, "CC:",cc, "PF:",pf
evalu = evaluate(pg, pf, ww, cc, n, m)
print "Paretto ->",noDominancia(evalu) 
#print evaluate(pg, pf, ww, cc, n, m)