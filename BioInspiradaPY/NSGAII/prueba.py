'''
Created on 14/06/2015

@author: JuanFelipe, Lin
'''
import numpy as np
from FirstGen import genFirst
from Evaluate import evaluate


n = 10
m = 2
inv = 2
pf = np.array([np.random.randint(100, size=n) for x in xrange(m)])
cc = np.random.randint(100, 150, size=m)
ww = np.random.randint(50, size=n)
pg = genFirst(inv, n, m)

print "PG:",pg, "WW:",ww, "CC:",cc, "PF:",pf

print evaluate(pg, pf, ww, cc, n, m)