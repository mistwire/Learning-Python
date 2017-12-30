# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 20:28:12 2017

@author: chris
"""
def problem3_3(month, day, year):
    """ Takes date of form mm/dd/yyyy and writes it in form June 17, 2016 
        Example3_3: problem3_3(6, 17, 2016) gives June 17, 2016 """
    months=("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    print (months[month-1] + ' ' + str(day) + ', ' + str(year))

