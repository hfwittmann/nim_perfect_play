#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 17:31:25 2017

@author: hfwittmann
"""

import numpy as np
import infix

#heapsIn = [1,2,5,7]
#heaps = heapsIn

def getBinaryRepresentation(heapsIn):
    
    assert np.max(heapsIn) < 256, \
        "Error all heaps must be smaller than 256, due to limits in the binary representation np.uint8"
    
    heaps = np.array(heapsIn, dtype=np.uint8).reshape(1, -1)
    out = np.unpackbits(heaps, axis=0)
    return out 

def getBalancing(heapsIn):
    
    binary = getBinaryRepresentation(heapsIn)
        
    #In [95]: getBinaryRepresentation([1,2,5,7])
    #Out[95]: 
    #array([[0, 0, 0, 0],
    #       [0, 0, 0, 0],
    #       [0, 0, 0, 0],
    #       [0, 0, 0, 0],
    #       [0, 0, 0, 0],
    #       [0, 0, 1, 1],
    #       [0, 1, 0, 1],
    #       [1, 0, 1, 1]], dtype=uint8)
    
    balancing = binary.sum(axis=1) % 2
    
    return balancing

@infix.or_infix
def NIM_PLUS(a, b):
    
    assert type(a) in [int, np.int64] , "both a and b must be integers"
    assert type(b) in [int, np.int64], "both a and b must be integers"
    out = NIM_SUM ([a,b])
    
    return int(out)

def NIM_SUM(xList):
    
    assert type(xList) in [list, np.ndarray], "xList must be a list or np.ndarray"
    balancing = getBalancing (xList)
        
    out = int(np.packbits(balancing))
    
    return int(out)


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

def find_largest_heap_with_power(heapsIn):
    
    heaps = np.array(heapsIn)
    
#    balancing =  getBalancing(heapsIn)
#    
##    highest_imbalanced_power = len(balancing) - 1 - np.argmax(balancing)
#    highest_imbalanced_power_index = np.argmax(balancing)

    bin_rep = getBinaryRepresentation(heapsIn) 
    
    myNimSum = NIM_SUM(heapsIn)
    
    if myNimSum == 0:
        return 'NIM SUM is 0, the position is losing'
    
    # find highest power of two less than then nim sum : NIM_SUM(heapsIn)
    highestPower_in_nim_sum = int(np.log2( NIM_SUM(heapsIn) ))
    # in bin_rep the lowest powers are at the bottom (ie = end = bin_rep.shape[0])
    highestPower =  bin_rep.shape[0] - 1 - highestPower_in_nim_sum
    
    # find those heaps that have have this highestPower_in_nim_sum in them 
    has_power_index = bin_rep[highestPower,:] == 1
    heaps_with_power_numbers = np.arange(len(heapsIn))[has_power_index]
    
    # now find the largest of those with power!
    largest = np.argmax(heaps[heaps_with_power_numbers])
    
    return heaps_with_power_numbers[largest]    
    

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
        
        largestHeapWithPower_index = find_largest_heap_with_power(heaps)        
        # always take from the largest heap, even in a losing position
        # This has advantages: It does not unecessarily remove complexity

        heapnumber = largestHeapWithPower_index
        
#        beansNumber = NIM_SUM ([heapsIn[heapnumber]] )
        newHeapsize = NIM_SUM(heapsIn) |NIM_PLUS| heapsIn[heapnumber]
        beansNumber = heapsIn[heapnumber] - newHeapsize
        
        
        
    heapsNext = heaps.copy()
    heapsNext[heapnumber] += -beansNumber
                
    out = { 'winning' : isWinning(heapsIn),
            'description': 'From heap {} take this number of beans : {}'.format(heapnumber, beansNumber),
            'move': [heapnumber, beansNumber],
            'next_position' : heapsNext,
            'position_before_move': heaps
            }     
            
    return out
            
            
        