# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 18:16:43 2016

@author: hfwittmann
"""
    
from unittest import TestCase
from nim_perfect_play.nim_perfect_play import findWinningMove, NIM_PLUS, NIM_SUM, find_heap_with_power

class TestConsole(TestCase):
    
    def test_find1(self):
        
        result1 = findWinningMove([1,21,1])
        
        #        {'description': 'From heap 1 take this number of beans : 21',
        #         'move': [1, 21],
        #         'next_position': array([1, 0, 1]),
        #         'winning': True}
        self.assertEqual(result1['move'], [1, 21])
    
    def test_find2(self):
        
        result1 = findWinningMove([1,3,5,6])
        
        #        {'description': 'From heap 3 take this number of beans : 1',
        #         'move': [3, 1],
        #         'next_position': array([1, 3, 5, 5]),
        #         'position_before_move': array([1, 3, 5, 6]),
        #         'winning': True}
        #        
        
        self.assertEqual(result1['move'], [0, 1])
        self.assertEqual(result1['winning'], True)
        
    def test_find3(self):
        
        result1 = findWinningMove([1,3,5,7])
        
        #        {'description': 'From heap 3 take this number of beans : 1',
        #         'move': [3, 1],
        #         'next_position': array([1, 3, 5, 5]),
        #         'position_before_move': array([1, 3, 5, 6]),
        #         'winning': True}
        #        
        
        self.assertEqual(result1['move'], [3, 1])
        self.assertEqual(result1['winning'], False)
        
    def test_find4(self):
        #  check self-consistency of alternating winning and losing positions
        
        # initialize
        done = False
        position = [1,3,5,7]
        
        winning = findWinningMove(position)['winning']
        previous_winning = not winning

        
        while not done:
            
            result = findWinningMove(position)
            
            next_position =  result['next_position']
            winning = result['winning']
            self.assertEqual(winning, not previous_winning, 
                             'If the previous position was winning, after an optimal move the new position should be lost, \
                              If the previous position was lost the new position should be winning. The position is : {}'.format(position))
        
            
            
        
            if sum(next_position) == 0:
                done = True
            
            print ('position :{}, next_position: {}, winning : {}, done: {}'.format(position, next_position, winning, done))
            
            
            position = next_position.copy()
            previous_winning = winning
            
    
    def test_find5(self):
        
        res = findWinningMove([3,4])

        self.assertEqual(res['winning'], True)
        self.assertEqual(res['move'], [1,1])
                

        res = findWinningMove([0,3,4])

        self.assertEqual(res['winning'], True)
        self.assertEqual(res['move'], [2,1])
                
        
        res = findWinningMove([0,0,3,4])

        self.assertEqual(res['winning'], True)
        self.assertEqual(res['move'], [3,1])
        
        
        res = findWinningMove([0,0,0,3,4])

        self.assertEqual(res['winning'], True)
        self.assertEqual(res['move'], [4,1])
                
        


    def test_NIM_PLUS(self):
        
        # associativity
        self.assertEqual( (3 |NIM_PLUS| 14) |NIM_PLUS| 25, \
                           3 |NIM_PLUS| (14 |NIM_PLUS| 25), \
                           ' |NIM_PLUS| is associative' )
        
        self.assertEqual( (13 |NIM_PLUS| 141) |NIM_PLUS| 252, \
                           13 |NIM_PLUS| (141 |NIM_PLUS| 252), \
                           ' |NIM_PLUS| is associative' )
        
        
        # commutativity
        self.assertEqual( 13 |NIM_PLUS| 24, \
                          24 |NIM_PLUS| 13 , \
                           ' |NIM_PLUS| is commutative' )
        
        
        self.assertEqual( 131 |NIM_PLUS| 241, \
                          241 |NIM_PLUS| 131 , \
                           ' |NIM_PLUS| is commutative' )
        
        
        # identity
        self.assertEqual( 0 |NIM_PLUS| 241, \
                                       241, \
                   '0 is the neutral (or identity) element' )

        
        # self-inverse
        self.assertEqual (3 |NIM_PLUS| 3, 0 , 'x |NIM_PLUS| x must be zero for all x')
        self.assertEqual (17 |NIM_PLUS| 17, 0 , 'x |NIM_PLUS| x must be zero for all x')



    def test_NIM_SUM(self):
        
        # commutativity
        self.assertEqual( NIM_SUM([13, 24]) , \
                          NIM_SUM([24, 13]) , \
                           ' NIM_SUM is commutative' )
        
        
        self.assertEqual( NIM_SUM([131, 242]) , \
                          NIM_SUM([242, 131]) , \
                           ' NIM_SUM is commutative' )
        
        # identity
        self.assertEqual( NIM_SUM([0, 242]) , \
                                       242  , \
                   '0 is the neutral (or identity) element' )
        
        # self-inverse
        self.assertEqual( NIM_SUM([3, 3]) , \
                                       0  , \
           'NIM_SUM([x, x] nust be zero for all x. Thus x is its own inverse.' )
               

    def test_heap_with_power(self):
        
        heap_index = find_heap_with_power ([1, 4, 8, 8])  
        #        In [157]: NIM_SUM([1, 4, 8, 8])
        #        Out[157]: 5
        
        #        In [154]: getBinaryRepresentation([1, 4, 8, 8, 5])
        #        Out[154]: 
        #        array([[0, 0, 0, 0, 0],
        #               [0, 0, 0, 0, 0],
        #               [0, 0, 0, 0, 0],
        #               [0, 0, 0, 0, 0],
        #               [0, 0, 1, 1, 0],
        #               [0, 1, 0, 0, 1],
        #               [0, 0, 0, 0, 0],
        #               [1, 0, 0, 0, 1]], dtype=uint8)
        
        # From the above we can see that the heap_index is 1
        self.assertEqual( heap_index, 1 )
        
        
        heap_index_2 = find_heap_with_power ([1, 4, 8, 8, 23])  
        
        #        In [162]: NIM_SUM([1, 4, 8, 8, 23])
        #        Out[162]: 18
        
        #        In [168]: getBinaryRepresentation([1, 4, 8, 8, 23, 18])
        #        Out[168]: 
        #        array([[0, 0, 0, 0, 0, 0],
        #               [0, 0, 0, 0, 0, 0],
        #               [0, 0, 0, 0, 0, 0],
        #               [0, 0, 0, 0, 1, 1],
        #               [0, 0, 1, 1, 0, 0],
        #               [0, 1, 0, 0, 1, 0],
        #               [0, 0, 0, 0, 1, 1],
        #               [1, 0, 0, 0, 1, 0]], dtype=uint8)
        
        # From the above we can see that the largest_heap_index is 4
        self.assertEqual( heap_index_2, 4 )
        
        
        
        
        
#        
# for simple debugging : self = TestConsole()        