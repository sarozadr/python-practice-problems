"""Author Arianna Delgado
Created on June 25, 2020
"""

"""Find commun elements of two list with a list comprehension"""

first_list = [1,2,3,4,5]
second_list = [5,6,7,8,9]

'''#Uses loop  to solve the proplem.
for i in first_list
    if i in second_list
        result.append(i)'''



#Uses list comprehension for solution.
new_list =[i for i in first_list if i in second_list]

print(new_list)