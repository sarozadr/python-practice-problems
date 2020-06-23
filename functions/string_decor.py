"""Author Arianna Delgado
Created on June 22, 2020
"""

"""Develops a function that will declarered strings
Hello function takes a name hello(name)
with a decoretor function Howareyou() that will take the result of hello() function 
and append how are at teh end """ 

#Declares a function that returns a function
def decorfun(fun):
    def inner(n):
        result = fun(n)
        result = result + " How are you?"
        return result
    return inner    


#Runs the function and teh return value is pass to the decorfun() 
@decorfun
def hello(name):
    return "Hello " + name


#Calls hello function 
print(hello("Arianna"))