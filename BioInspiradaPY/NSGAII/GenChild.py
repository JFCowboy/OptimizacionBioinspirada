'''
Created on 15/06/2015

@author: JuanFelipe, Lin
'''
import numpy as np

def competir( p1, p2, pareto1, pareto2, crow1, crow2):
    ret = -1;
    if pareto1 < pareto2:
        ret = p1
    elif pareto1 > pareto2:
        ret = p2
    elif crow1 > crow2:
        ret = p1
    else:
        ret = p2
    
    return ret;


def tournament( inv, pareto, crow):
    #print inv, pareto, crow
    nInv    = len( inv )
    p1, p2  = -1, -1
    g1, g2  = -1, -1
    p3, p4  = -1, -1
    nTorneos= nInv / 2
    pairs = [] 
    for i in xrange( nTorneos ):
        p1 = np.random.randint(0,nInv)
        p2 = np.random.randint(0,nInv)     
        while p1==p2 :
            p2 = np.random.randint(0,nInv)
            
        g1 = competir(p1, p2, pareto[p1], pareto[p2], crow[p1], crow[p2])
        
        p3 = np.random.randint(0,nInv)
        while p3==g1 :
            p3 = np.random.randint(0,nInv)
            
        p4 = np.random.randint(0,nInv)        
        while p3==p4 or p4==g1 :
            p4 = np.random.randint(0,nInv)
        g2 = competir(p3, p4, pareto[p3], pareto[p4], crow[p3], crow[p4])
        pairs.append( (g1, g2) )
    
    return pairs

def mutation(indiv,N, M):
    #print indiv
    mutateGen = np.random.randint(indiv.size)
    
    indiv[mutateGen] = np.random.randint(M)    
    return indiv
    
#a = [0,2,4,5]
#mutation(a,4)

def reproduction(indiv1,indiv2, Otro):
    N = len( indiv1 )
    indivAux = indiv1
    #print "-:_:-",indiv1[:N/2], indiv2[N/2:], indivAux
    
    indiv1 = np.append(indiv1[:N / 2] , indiv2[(N / 2) :], axis=0)#indiv1[:N / 2] + indiv2[(N / 2) :]
    #print "-:::::-",indiv1 
    indiv2 = np.append(indiv2[:N / 2] , indivAux[(N / 2) :], axis=0)#indiv2[:N / 2] + indivAux[(N / 2) :]
    #print indiv1, indiv2
    return indiv1, indiv2

def genChild( inv, pareto, crow, N, M, probMutar):
    tam = len( inv )
    
    if tam%2==1:
        print "El tamano no es par"
        
    pairs = tournament(inv, pareto, crow)
    #print "Parejas", pairs
    children = None
    for (x, y) in pairs:
        #print "Padres", inv[x], inv[y], x, y
        e1, e2 = reproduction(inv[x], inv[y], N)
        #print "hijos", e1, e2
        if children == None:
            children = np.array( [e1] )
        else:
            children = np.append( children, [e1], axis = 0 )
        children = np.append( children, [e2], axis = 0 )
    
    #print "Childrens", children
    for idx, x in enumerate( children ):
        rand = np.random.randint(0, 100); 
        if( rand<probMutar ):
            children[idx] = mutation(x, N, M)
        
    return children
    
def selection(inv, pareto, crow):
    aux = [(index, pareto[index], crow[index]) for index in xrange(len(inv))]
    aux = sorted(aux, key = lambda ar: (ar[1], ar[2]))
    pairs = []
    i = 0
    while( i < len(inv) ):
        pairs.append( ( aux[i][0], aux[i+1][0]) )
        i+=2
    return pairs

def genChild2( inv, pareto, crow, N, M, probMutar):
    tam = len( inv )
    
    if tam%2==1:
        print "El tamano no es par"
        
    pairs = selection(inv, pareto, crow)
    print "Parejas", pairs
    children = None
    for (x, y) in pairs:
        #print "Padres", inv[x], inv[y], x, y
        e1, e2 = reproduction(inv[x], inv[y], N)
        #print "hijos", e1, e2
        if children == None:
            children = np.array( [e1] )
        else:
            children = np.append( children, [e1], axis = 0 )
        children = np.append( children, [e2], axis = 0 )
    
    #print "Childrens", children
    for idx, x in enumerate( children ):
        rand = np.random.randint(0, 100); 
        if( rand<probMutar ):
            children[idx] = mutation(x, N, M)
        
    return children