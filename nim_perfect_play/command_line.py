# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 17:29:35 2016

@author: hfwittmann
"""

import argparse
import sys

import nim_perfect_play


def main():
    

    parsed_args = myparse_args(sys.argv[1:])
    
    out = nim_perfect_play.findWinningMove(parsed_args.Heaps)
    
    return out


# https://stackoverflow.com/questions/18160078/how-do-you-write-tests-for-the-argparse-portion-of-a-python-module
def myparse_args(args):
    
    ''' Example of taking inputs'''
    
    parser = argparse.ArgumentParser(prog = 'my nim program')
    
    # https://stackoverflow.com/questions/2086556/specifying-a-list-as-a-command-line-argument-in-python
    # parser.add_option("-t", "--tracks", action="append", type="int")
    
    
    parser.add_argument('-H', '--Heaps', nargs='*', type =int, help = 'help for -Heaps : This expects the heaps as a vector')
#    parser.add_argument('unittest_args', nargs='*')
    
    args_parsed = parser.parse_args(args)
    
    return args_parsed