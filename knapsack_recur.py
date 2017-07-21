# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 14:03:37 2017

@author: 
"""

def maxVal(toConsider, avail):
    """ Assumes toConsider is a list of items, avail is a weight.
        Returns a tuple of the total value of a solution to the 0/1 
        knapsack problem and the items of that solution"""
    
    #toConsider: the items that nodes higher up in the tree have not yet
    #considered
    
    #avail: the amount of space still available
    
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif avail - toConsider[0].getCost() < 0:
        #if item 0 is too heavy, skip and move on to consider the next item,
        #with the same availability.
        result = maxVal(toConsider[1:], avail)
    else:
        #examine two possibilites, one taking item 0, and one leaving it.
        #Associate each decision with a value (withVal, withoutVal), and compare
        #the two.  
        
        #nextItem = toConsider[0]
        
        #what results from taking the item?
        #ans: the max value obtained by considering the remaining items 
        #(calculated by calling maxVal again, this time reducing availability
        #by item's cost), plus the value of the item itself.  THe total is 
        #stored in withVal
        withVal, withToTake = maxVal(toConsider[1:], avail - toConsider[0].getCost())
        
        withVal += toConsider[0].getValue()
        
        #what results from not taking the item?
        #Again, the maxVal obtained by calling maxVal on the remainder of the
        #list, this time not reducing avail because we didn't take the item.
        #We also don't add anything to this consequent value because we're not
        #taking the item in question.
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        
        #Now compare the consequences
        if withVal > withoutVal:
            result = (withVal, (toConsider[0],) + withToTake)
            
        else:
            result = (withoutVal, withoutToTake)
    
    
    return result