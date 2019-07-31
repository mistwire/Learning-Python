# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 16:21:07 2017

@author: chris

Sample run using the list hourly_temp. Note that the grader will use a
different hourly list.  Be sure that you function works on this list and test
it on at least one other list of your own construction.
Note also, that the list the grader uses may not have the same number of items 
as this one.

problem2_8(hourly_temp)
Average: 38.791666666666664
High: 48.0
Low: 32.0
"""
def problem2_8(temp_list):
    sum_ = 0
    for i in temp_list:
        sum_ += i
    print('Average:', sum_/len(temp_list))
    print('High:', max(temp_list))
    print('Low:', min(temp_list))