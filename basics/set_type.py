"""Author Ariannna Delgado
Created on May 15, 2020
"""

#SET and FROZEN SET
#set does not allow duplicates
set1={10,20,30,'xyz'}
print(set1)
print(type(set1))


#does not care about duplicates; does not count duplicates
set2={10,20,30,'xyz', 10, 10}
print(len(set2))


#add elements to the set
set1.update([88,99])
print(set1)

# we can not perform indexing, slicing or repetition

#remove the value
set1.remove(10)
print(set1)


#convert a set to a frozen set
#you can not perform any other remove or update method
#we can navigate and retrieve the elements
f = frozenset(set1)
#f.update([20])
#f.remove(30)