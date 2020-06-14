"""Author Arianna Delgado
Created on July 14, 2020
"""

#This function takes two numbers.
def calc(a,b):
    w = a + b
    x = a - b
    y = a * b
    z = a / b
    return w, x,y,z

#This prints results
result = calc(10,5)
print(result)    

#Ways to print results
for i in result: 
    print (i)
