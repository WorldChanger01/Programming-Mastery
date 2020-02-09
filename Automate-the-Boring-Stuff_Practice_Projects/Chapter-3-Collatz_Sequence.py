# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 18:18:07 2020

@author: WorldChanger
"""
from sys import exit

def collatz(number):
    if number<0:
        print("Enter an intger please")
        exit()
    else:
        if number % 2 == 0:
            value=number // 2
            return value
        elif number % 2 == 1:
            value=3 * number + 1
            return value
        
try:
    print("Enter number:")
    user_input=int(input())
    b=collatz(user_input)
    
    while True:
        if b!=1:
            print(b)
            b=collatz(b)
        else:
            print(b)
            break
        
except ValueError:
    print("You must enter an integer")
    


        