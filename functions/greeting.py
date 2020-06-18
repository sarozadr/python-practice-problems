"""Author Arianna Delgado
Created on July 18, 2020
"""


#Defines a function inside another function.
def display(name):
    #this function will only be ablalible to access inside the function display.
    def message():
        return "Hello "
    result = message() + name 
    return result    


print(display("Arianna"))
#This will not be execute because the function message() can only be acccess from inside display() function.
#print(message())    