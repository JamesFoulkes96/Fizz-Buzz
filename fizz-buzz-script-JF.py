# -*- coding: utf-8 -*-
"""
Fizz Buzz - James Foulkes - January 2022
"""

### FUNCTION 
def Fizz_Buzz(f = 3, b = 5, n = 100):
    '''prints integers from 1 to n
    replacing multiples of f with "FIZZ",
    multiples of b with "BUZZ" and 
    multiples of both with "FIZZ-BUZZ!".'''
    
    for i in range(1, n + 1):
        if i%(f) == 0 and i%(b) == 0:
            print("FIZZ-BUZZ!")
        elif i%f == 0:
            print("FIZZ")
        elif i%b == 0:
            print("BUZZ")
        else:
            print(i)

### Get inputs
f = int(input("Fizz value: "))
b = int(input("Buzz value: "))
n = int(input("Upto: "))

### Run function
Fizz_Buzz(f, b, n)
