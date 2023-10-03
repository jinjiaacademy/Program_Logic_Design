# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 09:42:21 2023

@author: Jinjia
"""

"""
Input -- Processing -- Output
"""

"""
The music purchase program
Pseudocode:
    
Input the number of songs you wish to download today: Songs
Compute the cost of the purchase: Set DollarPrice = 0.99 * Songs
Display the value of DollarPrice

Declare Songs As Integer
Declare DollarPrice As Float

Write "Enter the number of songs you wish to purchase: "
Input Songs
Set DollarPrice = 0.99 * Songs
Write DollarPrice

Keywords: 
    Input & Output: Write, Input 
    Processing: Set
    Data Type: Declare
"""
# Songs = int(input("Enter the number of songs you wish to download today: "))
# DollarPrice = 0.99 * Songs
# print(f"{Songs} songs will cost $ {DollarPrice:.2f}")
# print(f"The number of songs to be downloaded is {Songs}")
# print(f"The cost for this purchase in dollars is {DollarPrice}")



"""
Write "Enter two numbers: "
Input Number1
Input Number2
Set Average = (Number1 + Number2) / 2
Write "The average of " + Number1 + " and " + Number2 + " is " + Average
"""

# Number1 = float(input("Enter the first number: "))
# Number2 = float(input("Enter the second number: "))
# Average = (Number1 + Number2) / 2
# print(f"The average of {Number1} and {Number2} is {Average}")

"""
Write "Enter temperature in degrees Fahrenheit to convert to Celsius: "
Input DegreesFahrenheit
Set DegreesCelsius = 5 * (DegreesFahrenheit - 32) / 9
Write DegreesFahrenheit + " degrees Fahrenheit converts to " + DegreesCelsius + "degrees Celsius"
"""

# DegreesFahrenheit = float(input("Enter temperature in degrees Fahrenheit to \
#                                 convert to celsius: "))
# DegreesCelsius = 5 * (DegreesFahrenheit - 32) / 9
# print(f"{DegreesFahrenheit} degrees Fahrenheit converts to {DegreesCelsius} degrees Celsius.")


"""
Declare Flag As Boolean
Declare Songs As Integer
Declare DollarPrice As Float

Set Flag = false
Write "Enter the number of songs you wish to purchase: "
Input Songs
If Songs < 0 Then
    Set Flag = true
If Flag is true Then
    Write "You cannot order a negative number of songs."
If Flag is false Then
    Set DollarPrice = 0.99 * Songs
    Write DollarPrice
    
"""