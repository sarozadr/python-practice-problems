"""Author Arianna Delgado
Created on June 18, 2020
"""

"""Using the MAP function double the value of each element in the list"""

list_num = [2,3,4,5]

#Takes a lambda expression and a sequence of pararmeters.
#Converts the map result to a list
result = list(map(lambda x: x * 2, list_num))

print(result)




