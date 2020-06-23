"""Author Arianna Delgado
Created on June 22, 2020
"""

"""A Generato is a sequence of values"""

#Defines a function passing two values
def customgen(x,y):
    while x < y:
        #Storages all the values of x in memory and at the end it will return 
        yield  x
        #Increaments the values of x until it reaches y-1
        x += 1


result = customgen(20,30)

for i in result: print(i)


