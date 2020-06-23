"""Author Arianna Delgado
Created on June 23, 2020
"""

"""Product of elements in two lists using list comprehension. """

#Decles three lists.
first_list = [1,2,3,4,5]
second_list = [6,7,8,9,10]
empty_list = []


#Uses traditional way to solve the proplem.
'''for i in range(len(first_list)):
    empty_list.append(first_list[i] * second_list[i])

print(empty_list)'''   


#Uses list comprehension for the solution.
empty_list = [ first_list[i] * second_list[i] for i in range(len(first_list))]
print(empty_list)



