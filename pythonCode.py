# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 09:42:21 2023

@author: Jinjia
"""

"""
The music purchase program
Pseudocode:
    
Input the number of songs you wish to download today: Songs
Compute the cost of the purchase: Set DollarPrice = 0.99 * Songs
Display the value of DollarPrice
"""
Songs = int(input("Enter the number of songs you wish to download today: "))
DollarPrice = 0.99 * Songs
print(f"{Songs} songs you wish to download today will cost ${DollarPrice}")