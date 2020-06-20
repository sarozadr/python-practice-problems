"""Author Arianna Delgado
Created on June 18, 2020
"""


#Pass a a function as a parameter to the function.
def display(fun):
    return "Hello " + fun

def name():
    return "Arianna"

#Calls the name() function and the results is pass to display() function and print the result.
print(display(name()))