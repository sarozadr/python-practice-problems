"""Author Ariannna Delgado
Created on May 28, 2020
"""

"""Showing List is mutable"""
l1 = [2,3,4,5,8,4,3,5,2,1,8,8,6,3,4,5,7,9]
set1 =(set(l1))
l2 = list(set1)
print(l2)

#list are mutable
l2[0] = 100
print(l2)




"""Showing tuples are immutable"""
#tuples are immutable
tuple1 = tuple(l2)
tuple1[0] = 1 #this line will trigger an error
print(tuple1)
