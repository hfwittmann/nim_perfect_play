#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 17:31:25 2017

@author: hfwittmann
"""

import functools
import numpy as np
import infix

#heapsIn = [1,2,5,7]
#heaps = heapsIn

@infix.or_infix
def NIM_PLUS(a, b):
    
    assert type(a) in [int, np.int64] , "both a and b must be integers"
    assert type(b) in [int, np.int64] , "both a and b must be integers"
    out = a ^ b
    
    return int(out)

def NIM_SUM(xList):
    
    assert type(xList) in [list, np.ndarray], "xList must be a list or np.ndarray"
    
    # https://stackoverflow.com/questions/14562991/python-equivalent-of-sum-using-xor
    out = functools.reduce(lambda a, b: a ^ b, xList, 0)
    
    return out


    #In [46]: 4 |NIM_PLUS| 4
    #Out[46]: 0
    
    # In [47]: NIM_SUM([4,4])
    # Out[47]: 0
    
    
def isWinning(heapsIn):
    # check if nim sum is not 0
    
    # if the nim sum is 0, 
    # then position is balanced - that is all coeeficients are zero - 
    # then it is a losing position
    
    winning = NIM_SUM(heapsIn) != 0
    
    return winning


def find_heap_with_power(heapsIn):
    
    # find a heap that is larger than the nimusum of the heap plus the total nimsum
    #  heap > heap ⊕([heaps])

    """ Quote from wikipedia:
       To find out which move to make, let X be the nim-sum of all the heap sizes. Find a heap where the nim-sum of X and
       heap-size is less than the heap-size - the winning strategy is to play in such a heap, reducing that heap to the nim
       sum of its original size with X. "
       
       https://en.wikipedia.org/wiki/Nim
    """
       
    myNimSum = NIM_SUM(heapsIn)
    
    if myNimSum == 0:
        return 'NIM SUM is 0, the position is losing'
    
    for heapIndex in range(len(heapsIn)):
        
        heapSize = heapsIn[heapIndex]
        
        if heapSize |NIM_PLUS| myNimSum < heapSize:
            
            return heapIndex # stops after the first found heap that satisfies the condition
    

def findWinningMove(heapsIn):
    
    # there maybe 0, 1 or more winning moves    
    heaps = np.array(heapsIn)
    
    if heaps.sum() == 0:
        return 'There are only 0 beans in total. This game has already finished.'
    
    # the position is a losing position, there is no winning move
    if not isWinning(heapsIn):
    
        # always take from the largest heap, even in a losing position
        # This has two advantages:
        # 1) It is not easily distinguishable from a winning move by a person/entity/agent 
        #      who does not (yet) know the winning strategy
        # 2) It does not unecessarily remove complexity, again an advatage against 
        #     a person/entity/agent who does not (yet) know the winning strategy
        
        # Also we only take one bean, to leave the situation as complex as possible
          
        largestHeap_number = np.argmax(heaps)
        
        beansNumber = 1
        
        heapnumber = largestHeap_number
    
    
    # the position is winning
    else:
    
        heapWithPower_index = find_heap_with_power(heaps)        
        # take from the largest heap, even in a losing position
        # This has advantages: It does not unecessarily remove complexity
        
        heapnumber = heapWithPower_index
        
        #        beansNumber = NIM_SUM ([heapsIn[heapnumber]] )
        newHeapsize = NIM_SUM(heapsIn) |NIM_PLUS| heapsIn[heapnumber]
        beansNumber = heapsIn[heapnumber] - newHeapsize
    
    
    
    heapsNext = heaps.copy()
    heapsNext[heapnumber] += -beansNumber
            
    out = { 'winning' : isWinning(heapsIn),
        'description': 'From heap {} take this number of beans : {}'.format(heapnumber, beansNumber),
        'move': [heapnumber, beansNumber],
        'next_position' : list(heapsNext),
        'position_before_move': list(heaps)
        }     
        
    return out