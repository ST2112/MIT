# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 18:14:16 2017

@author: 
"""
def fib_memo(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    
    try:
        return memo[n]
    except KeyError:
        result = fib_memo(n-1, memo) + fib_memo(n-2, memo)
        memo[n] = result
        return result

