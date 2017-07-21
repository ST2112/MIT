# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 15:09:57 2017

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

def greedy(items, maxWt, keyFunction):
    
    sortedItems = sorted(items, key = keyFunction, reverse = True)
    
    knapsack = []
    totalWeight = 0.0
    totalValue = 0.0
    for i in range(len(sortedItems)):
        if totalWeight + sortedItems[i].getWeight() <= maxWt:
            knapsack.append(sortedItems[i])
            totalWeight += sortedItems[i].getWeight()
            totalValue += sortedItems[i].getPrice()
            
    return (totalValue, totalWeight, knapsack)
     
def testGreedy(items, constraint, keyFunction):
    val, wt, solution = greedy(items, constraint, keyFunction)
    
    
    for i in solution:
        print(i)
        
    print("Total value of shipment: " + str(val))
    print("Total weight of shipment: " + str(wt))
        
def testGreedys(items, constraint):
    print('Greedy by price for total shipment <= ' + str(constraint) + ' lbs')
    testGreedy(items, constraint, Bovine.getPrice)
    
    print('Greedy by $/lb for total shipment <= ' + str(constraint) + ' lbs')
    testGreedy(items, constraint, lambda x: Bovine.getPrice(x)/Bovine.getWeight(x))
