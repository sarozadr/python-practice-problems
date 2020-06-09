"""Author Ariannna Delgado
Created on May 15, 2020
"""

#BYTES AND ARRAYS


list1= [20,30,40,234]
print(type(list1))

b= bytes(list1)
print(type(b))

#you can not add or indexing  elements to bytes
#b[3]= 45


#you can modified and add elements to the byte array
b1 = bytearray(list1)
print(type(b1))
#add value through indexing to the byte array
b1[3] = 24
print(b1)
"""why I can not print an byte array?"""