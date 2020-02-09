# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:48:51 2020

@author: WorldChanger
"""

def comma_code(somelist):
    s=''
    for i in range(len(somelist)):
        if i <= len(somelist)-3:
            s = s + str(somelist[i]) + "," + " "
        elif i == len(somelist)-2:
            s = s + str(somelist[i]) + " and  "
        else:
            s = s + str(somelist[i])
    return "'"+ s + "'"

somelist=["apple", "banana", "pear", 1, 3, 4, 5, 6]        

print(comma_code(somelist))