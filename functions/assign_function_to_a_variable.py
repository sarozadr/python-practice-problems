"""Author Arianna Delgado
Created on June 18, 2020
"""

x = 123

#Declares a function.
def result():
    x = 30 
    print(x)
    print(globals()['x'])


#This asssing a function to a variable.
y = result
y()
y()