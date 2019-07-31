# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 20:13:04 2017

@author: chris
"""

def problem1_7():
    b1 = float(input('Enter the length of one of the bases: '))
    b2 = float(input('Enter the length of the other base: '))
    h = float(input('Enter the heigt: '))
    area = (1/2)*(b1+b2)*h
    print('The area of a trapezoid with bases',b1,'and',b2,'and height',h,'is',area)