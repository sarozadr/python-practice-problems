"""Author Arianna Delgado
Created on July 14, 2020
"""


#This is a Global Variable.
#Can be access any where.
x = 123
print(x)

def display():
    #Declares local variable.
    y = 456
    print(x)

#This variable value can not be access, because it inside the  display() function.
#print(y)
#display()

#Displays the value of x two times first and then call display() function
print(x)
display()
