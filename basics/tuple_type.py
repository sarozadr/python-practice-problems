"""Author Arianna Delgado
Created on May 15, 2020
"""

#TUPLE 
#it is like a list but it can not be modified using ()
# can not used methods like append(), extend(), insert(), remove(), clear()
tuple1 = (40,50,40,'xyz')
print(tuple1)
print(tuple1[3])
print(tuple1*4)
print(tuple1.count(40))
print(tuple1.index("xyz"))

#if you want to declare a list or tuple with only one element use ,
tuple2 = (40,)
list3 = [30,]


#create a list
list4=[20,30,'xyz']
print(list4)
#convert  a list to a tuple
tuple3 = tuple(list4)
print(type(tuple3))
