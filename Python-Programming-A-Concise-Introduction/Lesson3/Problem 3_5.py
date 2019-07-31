# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 20:52:57 2017

@author: chris
"""

def problem3_5(name):
    """ Looks up the phone number of the person whose name is name """
    
    phone_numbers = {"abbie":"(860) 123-4535", "beverly":"(901) 454-3241", \
                      "james": "(212) 567-8149", "thomas": "(795) 342-9145"}
    print(phone_numbers[name])