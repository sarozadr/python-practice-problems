"""Author Arianna Delgado
Created on July 1, 2020
"""

#Creates a class Product.
class Product:

    #Constructor function, with init built function.
    #Self points to the correct object that is being created. 
    def __init__(self):
        #Declares and assigns values for the class file. 
        self.name = 'IPhone'
        self.price = 700
        self.description = 'Its awesome'

#Creates an object of this class. To invoke the init function.
p1 = Product()

#Access values.
print(p1.name)
print(p1.price)
print(p1.description)

#Create a second object of the class Product.
p2 = Product()

#Access values.
print(p2.name)
print(p2.price)
print(p2.description)



