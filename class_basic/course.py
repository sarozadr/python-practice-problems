"""Author Arianna Delgado
Created on July 1, 2020
"""

#Creates a class Product.
class Course:

    #Constructor function, with init built function.
    #Self points to the correct object that is being created.
    def __init__(self,name, ratings):
        #Declares and assigns values for the class file. 
        self.name = name
        self.ratings = ratings

    def average(self):
        number_of_ratings = len(self.ratings)
        average = sum(self.ratings)/number_of_ratings
        print("Average rating for ", self.name, "is ", average)



#Creates an object of this class. To invoke the init function.
c1 = Course("Java Course ", [1,2,3,4,5])

print(c1.name)
print(c1.ratings)
#Constructor calls average function.
c1.average()


#Create a second object of the class Product.
c2 = Course("Java Web Services ", [5,5,5,5,5])

print(c2.name)
print(c2.ratings)
#Constructor calls average function.
c2.average() 



