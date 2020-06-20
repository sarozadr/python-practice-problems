"""Author Arianna Delgado
Created on June 14, 2020
"""

#This function takes two numbers.
def calc(a,b):
    w = a + b
    x = a - b
    y = a * b
    z = a / b
    return w, x,y,z

#This prints results of calculation.
result = calc(10,5)
print(result)    

#Ways to print results one by one.
for i in result: 
    print (i)
