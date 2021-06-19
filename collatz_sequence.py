# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 12:21:15 2021

@author: Cleme
"""
#! python3
# collatz.py - Number is evaluated as odd or even and is then evaluated 
# down to one

import sys

# Define the collatz sequence
def collatz(number): 

    if number % 2 == 0: 
        print(number // 2)
        return number // 2
    elif number % 1 == 0: 
        result = 3 * number + 1
        print(result)
        return result
    else: 
        print('Something went wrong, please type in a different number.')


n = int(input('Please type in a number:\n'))


try: 
    while n != 1:
        n = collatz(n)
        
except KeyboardInterrupt: 
    print('Something went wrong. Please try again.')
    sys.exit()

    

    
    
    



    

