"""Author Arianna Delgado
Created on July 18, 2020
"""

"""Use the filter function and retrieve only even numbers from a given list of numbers."""

list_num = [10,2,33,45,89,2]


#Takes two parameters: lambda expresion and sequence.
#Converts the result into a list.
result = list(filter(lambda x: x % 2 == 0, list_num))

print(result)




