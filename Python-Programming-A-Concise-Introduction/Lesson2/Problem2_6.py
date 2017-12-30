# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 15:46:53 2017

@author: chris
"""
import random

def problem2_6():
    """ Simulates rolling 2 dice 100 times """
    # Setting the seed makes the random numbers always the same
    # This is to make the auto-grader's job easier.
    random.seed(431)  # don't remove when you submit for grading
    for i in range(100):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        sum_ = d1 + d2
        print(sum_)
