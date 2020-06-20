"""Author Arianna Delgado
Created on July 18, 2020
"""

"""Using the reduce function to find out the sum of all the elements in a list."""
"""Import the reduce model"""

from functools import reduce

list_num = [5,10,15,20]


#Takes a function and a sequence.
result = reduce(lambda x,y: x + y, list_num)

print(result)

