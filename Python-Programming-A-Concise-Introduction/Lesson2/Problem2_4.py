# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 15:18:49 2017

@author: chris
"""

import random

def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    rr = list()
    random.seed(70)
    for i in range(0,10):
        num_ = (random.random()*5) + 30
        rr.append(num_)

    print(rr)
