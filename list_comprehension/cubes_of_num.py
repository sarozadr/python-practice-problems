"""Author Arianna Delgado
Created on June 23, 2020
"""

"""List comprehensions easy to use sintax, 'short' to create one list out of another applying logic or conditions.
l = [expression for item in interable if condition] we loop through a list, 
expression can be a lambda expression with is the logic that will be applying to the list.
The resulting list will contain the values if the condition is satisfied."""

"""Use list comprehension to calculate the cube of integer from 1 to 10"""


#Uses loop  to solve the proplem.
'''new_list = []

for x in range(1,11):
    new_list.append(x**3)

print(new_list)'''    


#Uses list comprehension: expression and interable operation
new_list = [x ** 3 for x in range(1, 11)]
print(new_list)



