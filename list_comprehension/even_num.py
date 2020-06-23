"""Author Arianna Delgado
Created on June 23, 2020
"""

"""Even numbers between 1 to 20 using list comprehension."""

'''even_list =[x for x in range(2,21,2)]
print(even_list)'''

#Works as a list comprehension: expresion, loop, condition.
even_list = [x  for x in range(1,21) if x % 2 == 0]
print(even_list)




