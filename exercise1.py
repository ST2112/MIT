# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 16:19:12 2017

@author: 
"""

# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        #each iteration starts anew with an empty bag.  Consider i as an N-bit
        #binary number, where 0 in the jth place means "item j is not in the 
        #combo for this i" and 1 means "item j is in the combo".
        combo = []
        for j in range(N):
            # test bit jth of integer i: if the jth bit is 1, the item goes 
            #into the bag.  For example, if i = 13 (considering the 14th subset
            #in the powerset), the bit representation is 001101 (assuming N=6
            #items).  So roll through all 6 bits and check whether each is 0 
            #or 1.  If 1, add to the combo.
            #
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo
        
        
#We do a similar approach here.  Must consider how to represent each of the 
#3**N combinations as a tertiary number.  Rather than get this representation
#explicitly, however, we note that the number would be N trits long, and 
#do an integer divide of i by successive powers of 3, ranging from 0 to j-1.
#This is effectively a "trit-shift" by j places.  Then we consider whether
#modular division of the result by 3 results in 1 or 2 and put the item into
#the respextive bag.  A 0 modular result means the item does not go into a bag.
def yieldAllCombos(items):
    N = len(items)
    #enumerate all 3**N combinations
    for i in range(3**N):
        bag1 = []
        bag2 = []
        
        for j in range(N):
            if (i // 3**j) % 3 == 1:
                bag1.append(items[j])
            elif (i // 3**j) % 3 == 2:
                bag2.append(items[j])
                
        
        yield (bag1, bag2)
        