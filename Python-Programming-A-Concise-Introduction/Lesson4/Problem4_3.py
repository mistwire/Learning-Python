# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 12:57:00 2017

@author: chris
"""

def problem4_3(product, cost):
    """ Prints the product name in a space of 25 characters, left-justified
        and the price in a space of 6 characters, right-justified"""
    print("{0:25}${1:>6.2f}".format(product,cost))