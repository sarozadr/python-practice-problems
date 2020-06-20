"""Author Arianna Delgado
Created on June 18, 2020
"""

#Defines a function inside another function.
def display():
    #This function message() will only be ablalible to access inside the function display().
    def message():
        return "Hello"
    return message


fun = display()
print(fun())
  



