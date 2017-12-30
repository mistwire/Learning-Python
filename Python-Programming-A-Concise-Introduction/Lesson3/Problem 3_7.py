# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 21:14:15 2017

@author: chris
"""

def problem3_7(csv_pricefile, flower):
    import csv
    f = open(csv_pricefile)
    for row in csv.reader(f):
        if flower == row[0]:
            print(row[1])
    f.close()