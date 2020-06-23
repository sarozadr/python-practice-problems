"""Author Arianna Delgado
Created on June 20, 2020
"""

"A decorator function is a function that return another function"

"""Doubles the number returned """

#Function that returns another function
def decor(fun):
    #Inner function 
    def inner():
        #Invokes fun()
        result = fun()
        return result * 2
    return inner


@decor
def num():
    return 5 


#If @decor if used not need to add all this
#Invokes () the decord function passing a function num()
#result_fun = decor(num)
#print(result_fun())

print(num())



