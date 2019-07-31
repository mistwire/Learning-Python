# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 20:08:28 2017

@author: chris
"""

def problem3_1(txtfilename):
    lines = open(txtfilename)
    ct = 0
    for line in lines:
        print(line, end="")
        ct = ct + len(line)
    print('\n')
    print('There are ' + str(ct) + ' letters in the file.')