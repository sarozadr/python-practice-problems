"""Author Ariannna Delgado
Created on May 15, 2020
"""

#LIST
#empty List[]
#any #s, list keep the order
list1 =[]
print(list1)

#add elements in a list
#different types of data in a list
#declare with []
list2 = [10,20,'Arianna', -1, 30.5]
print(list2)
#print value in position 3; start from zero!
print(list2[3])
#you can use slicing and spacing at the list
print(list2[3:5])

#repeat the list 4 time
print(list2*4)
print(len(list2))

#add elements to a list
list2.append('new')
print(list2)

#remove an element from a  list; it case sensitive
list2.remove('Arianna')
print(list2)

#delete the index value
del(list2[0])
print(list2)
print(len(list2))

#clear a list elements
list2.clear()
print(list2)


#insert elements in a list
list2.insert(0, 10)
list2.insert(0, 20)
list2.insert(0, 50)
list2.insert(0, -1)
list2.insert(0, 30.5)
print(list2)

#print max and min in a list
print(max(list2))
print(min(list2))

#order  a list small to bigger
list2.sort()
print(list2)

#order a list from bigger to small
list2.sort(reverse = True)
print(list2)


#TUPLE it is like a list but it can not be modified using ()
# can not used methods like append(), extend(), insert(), remove(), clear()

















