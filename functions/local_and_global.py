"""Author Arianna Delgado
Created on June 14, 2020
"""


#This is a Global Variable.
#Can be access any where.
x = 123


def display():
    #Declares local variable that can only be acccess inside the function.
    y = 456
    print(y)
    #Calls x as a global variable
    print(globals()['x'])

#This variable value can not be access, because it inside the  display() function.
#print(y)
#display()

#Calls the global variable.
print(x)
#Calls the the function display().
display()
