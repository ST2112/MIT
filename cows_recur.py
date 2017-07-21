# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 17:08:08 2017

@author: 
    
"""
import random

class Bovine(object):
    def __init__(self, gen, tag, wt, prc):
        self.gender = gen
        self.earTag = tag
        self.weight = wt
        self.price = prc
        
    def getGender(self):
        return self.gender
    
    def getEarTag(self):
        return self.earTag
    
    def getWeight(self):
        return self.weight
    
    def getPrice(self):
        return self.price
    
#    def getUnitPrice(self):
#        return self.price/self.weight
    
    def __str__(self):
        return '<' + self.getGender() + ' #' + str(self.getEarTag()) + ': '\
                + str(self.getWeight()) + ' lbs. $' + str(self.getPrice()) + '>'
                
                
def buildHerd(N, maxTag, minWt, maxWt, minPrc, maxPrc):
    herd = []
    for i in range(N):
        coinFlip = random.randint(1,2)
        if coinFlip == 1:
            gender = 'heifer'
        else:
            gender = 'bull'
            
        tag = random.randint(1,maxTag)
        wt = random.randint(minWt, maxWt)
        prc = random.randint(minPrc, maxPrc)
        
        herd.append(Bovine(gender, tag, wt, prc))
        
    return herd

def maximizeVal(remainingItems, capacity):
    
    
    if remainingItems == [] or capacity == 0:
        result = (0.0, 0.0, ())
    elif remainingItems[0].getWeight() > capacity:
        result = maximizeVal(remainingItems[1:], capacity)
    else:
        itemConsidered = remainingItems[0]
        valIfTake, wtIfTake, shipIfTake = maximizeVal(remainingItems[1:],\
                                          capacity - itemConsidered.getWeight())
        
        valIfTake += itemConsidered.getPrice()
        wtIfTake += itemConsidered.getWeight()
        
        valIfLeave, wtIfLeave, shipIfLeave = maximizeVal(remainingItems[1:], capacity)
        
        if valIfTake > valIfLeave:
            result = (valIfTake, wtIfTake, (shipIfTake + (itemConsidered,)))
        else:
            result = (valIfLeave, wtIfLeave, shipIfLeave)
            
        
            
    return result