# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 15:08:58 2017

@author: chris
"""

alist = ["a","e","i","o","u","y"]
blist = ["alpha", "beta", "gamma", "delta", "epsilon", "eta", "theta"] 

def problem2_2(my_list):
    print(my_list)
    print(my_list[0])
    print(my_list[-1])
    print(my_list[3:5])
    print(my_list[:3])
    print(my_list[3:])
    print(len(my_list))
    my_list.append('z')
    print(my_list)
    