# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 18:16:43 2016

@author: hfwittmann
"""
    
import sys, argparse
    
from unittest import TestCase
from nim_perfect_play.command_line import main, myparse_args

class TestConsole(TestCase):
    
    def test_parser(self):
        
        parsed = myparse_args(['--Heaps', "1", "2", "31"])
        self.assertEqual(parsed.Heaps, [1,2,31])



    def test_commandline(self):
        
        sys.argv[1:] = ['--Heaps', '1','2','32'  ]
        output = main()
        
        self.assertEqual( {'winning': True, 
                            'description': 'From heap 2 take this number of beans : 29', 
                            'move': [2, 29], 
                            'next_position': [1, 2, 3], 
                            'position_before_move': [ 1,  2, 32]}, 
                             output,
                            'Should be equal')
#        
# for simple debugging : self = TestConsole()