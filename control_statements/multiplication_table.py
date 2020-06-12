"""Author Arianna Delgado
Created on May 28, 2020
"""


"""Multiplication table of a number entered by the user up to 10"""

num = int(input("Please, enter a number from 0 to 10: "))

for i in range(0,11):
    mult = num *i
    print(num, "X", i, "=", mult)
    
    
    
    
    