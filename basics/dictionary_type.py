"""Author Arianna Delgado
Created on May 15, 2020
"""

#DICTIONARY{} key + value

dic1 = {1:"John", 2:"Bob", 3:"Bill"}
print(dic1)


#to print key an values
print(dic1.items())


#keys
k = dic1.keys()
for i in k:
    print(i)
    
#values
v= dic1.values()
for i in v:
    print(i)
    
    
#passing the key we can get the value back
print(dic1[3])    

#delect a value in the dicionary
del dic1[3]
print (dic1)