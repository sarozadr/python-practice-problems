"""Author Arianna Delgado
Created on July 14, 2020
"""

""" Recursion"""

"""The same logic is repeated multiple times until the condition to stop the program is meet"""

def factorial(n):
    #Handles the last condition.
    if n == 0:
        result = 1
    else:  
        #This is where recursion happens, invoking the same function by reducing the n-1 
        result =  n * factorial(n-1)  
    return result        


print(factorial(5))