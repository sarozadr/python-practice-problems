"""Author Arianna Delgado
Created on June 23, 2020
"""

"""Even numbers between 1 to 20 using list comprehension."""

even_list = [x % 2 == 0 for x in range(1,21)]
print(even_list)
