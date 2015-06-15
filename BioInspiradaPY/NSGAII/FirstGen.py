'''
Created on 14/06/2015

@author: JuanFelipe
'''
import numpy as np
import random
from numpy.matlib import zeros

first = np.array([ [0,0,0] ])
print first

for x in xrange(10):
    first = np.append(first, [ [1, 2, 3] ], axis=0)

print first